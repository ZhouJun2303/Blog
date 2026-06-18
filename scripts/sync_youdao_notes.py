#!/usr/bin/env python3
"""
Sync public Youdao Note share links into the local Gridea posts.

The script treats remote note content as untrusted data. It parses only the
known Youdao XML / new-editor JSON structures and writes Markdown plus local
resource files.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
import sys
import time
import uuid
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Any, Dict, List, Tuple
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
POST_IMAGES_DIR = ROOT / "post-images"
POSTS_JSON = ROOT / "config" / "posts.json"

SHARE_KEY_RE = re.compile(r"id=([0-9a-fA-F]{32})")
FRONT_MATTER_RE = re.compile(r"\A(---\r?\n.*?\r?\n---\r?\n)(.*)\Z", re.S)
XML_NS = {"n": "http://note.youdao.com"}


@dataclass(frozen=True)
class NoteTarget:
    post_file: str
    url: str

    @property
    def slug(self) -> str:
        return Path(self.post_file).stem


TARGETS = [
    NoteTarget("an-zhuo-chang-jian-wen-ti-.md", "https://note.youdao.com/s/GLwOleTm"),
    NoteTarget("dao-chu-xcode-gong-cheng-jie-hao-sdk-ru-he-geng-xin.md", "https://note.youdao.com/s/d3aB0JW2"),
    NoteTarget("guan-yu-unitybuild-mo-ban-shi-yong.md", "https://note.youdao.com/s/53kLYfdi"),
    NoteTarget("hei-ping-guo.md", "https://note.youdao.com/s/P4UWBFXq"),
    NoteTarget("strip-engine-code.md", "https://note.youdao.com/s/Vuj663Xg"),
    NoteTarget("unityczhuan-dll.md", "https://note.youdao.com/s/V0wIfI58"),
]


class SyncError(RuntimeError):
    pass


class ResourceStore:
    def __init__(self, slug: str, dry_run: bool = False) -> None:
        self.slug = slug
        self.dry_run = dry_run
        self.image_index = 0
        self.attachment_index = 0
        self.downloaded: List[str] = []
        self.skipped: List[str] = []

    def download_image(self, url: str) -> str:
        self.image_index += 1
        return self._download(url, f"youdao-{self.slug}-{self.image_index:02d}", is_image=True)

    def download_attachment(self, url: str, filename: str) -> str:
        self.attachment_index += 1
        safe = sanitize_filename(filename) or f"attachment-{self.attachment_index:02d}"
        stem = f"youdao-{self.slug}-attachment-{self.attachment_index:02d}-{Path(safe).stem}"
        suffix = Path(safe).suffix
        try:
            return self._download(url, stem, is_image=False, preferred_suffix=suffix)
        except Exception as exc:
            self.skipped.append(f"{filename}: {exc}")
            return url

    def _download(
        self,
        url: str,
        stem: str,
        *,
        is_image: bool,
        preferred_suffix: str = "",
    ) -> str:
        if not is_allowed_youdao_url(url):
            raise SyncError(f"Refusing non-Youdao resource URL: {url}")

        req = urllib.request.Request(url, headers=request_headers())
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            content_type = resp.headers.get("Content-Type", "").split(";", 1)[0].strip()

        if preferred_suffix:
            suffix = preferred_suffix
        elif is_image:
            suffix = extension_from_bytes(data) or extension_from_content_type(content_type)
        else:
            suffix = extension_from_content_type(content_type) or extension_from_bytes(data)
        if not suffix:
            suffix = ".jpg" if is_image else ".bin"

        out_path = POST_IMAGES_DIR / f"{stem}{suffix}"
        if not self.dry_run:
            POST_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(data)

        rel = f"/post-images/{out_path.name}"
        self.downloaded.append(rel)
        return rel


def request_headers(referer: str = "https://share.note.youdao.com/") -> Dict[str, str]:
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"
        ),
        "Referer": referer,
    }


def fetch_text(url: str, referer: str = "https://share.note.youdao.com/") -> str:
    if not is_allowed_youdao_url(url):
        raise SyncError(f"Refusing non-Youdao URL: {url}")
    req = urllib.request.Request(url, headers=request_headers(referer))
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
    return raw.decode(charset, errors="replace")


def is_allowed_youdao_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        return False
    host = parsed.netloc.lower()
    return host.endswith("youdao.com") or host.endswith("ydstatic.com")


def extension_from_content_type(content_type: str) -> str:
    if content_type == "image/jpeg":
        return ".jpg"
    if content_type == "image/png":
        return ".png"
    if content_type == "image/gif":
        return ".gif"
    if content_type == "image/webp":
        return ".webp"
    return mimetypes.guess_extension(content_type) or ""


def extension_from_bytes(data: bytes) -> str:
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    if data.startswith(b"<?xml") or data.lstrip().startswith(b"<"):
        return ".xml"
    return ""


def sanitize_filename(name: str) -> str:
    name = unescape(name or "").strip()
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name[:120]


def resolve_share_key(short_url: str) -> str:
    req = urllib.request.Request(short_url, headers=request_headers())
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    with opener.open(req, timeout=60) as resp:
        final_url = resp.geturl()
        body = resp.read().decode(resp.headers.get_content_charset() or "utf-8", errors="replace")

    match = SHARE_KEY_RE.search(final_url) or SHARE_KEY_RE.search(body)
    if not match:
        raise SyncError(f"Could not resolve share key for {short_url}")
    return match.group(1)


def fetch_note_payload(share_key: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    unlogin_id = uuid.uuid4().hex
    referer = f"https://share.note.youdao.com/ynoteshare/index.html?id={share_key}&type=note"
    meta_url = (
        "https://note.youdao.com/yws/api/personal/share"
        f"?method=get&shareKey={share_key}&unloginId={unlogin_id}"
    )
    content_url = (
        f"https://note.youdao.com/yws/api/note/{share_key}"
        f"?sev=j1&editorType=1&unloginId={unlogin_id}"
        "&ignoreOwnPassword=false&editorVersion=new-json-editor"
    )

    meta = json.loads(fetch_text(meta_url, referer))
    content = json.loads(fetch_text(content_url, referer))
    return meta, content


def text_from_node(node: ET.Element, child_name: str = "text") -> str:
    child = node.find(f"n:{child_name}", XML_NS)
    return child.text if child is not None and child.text is not None else ""


def xml_to_markdown(content: str, store: ResourceStore) -> str:
    root = ET.fromstring(content)
    body = root.find("n:body", XML_NS)
    if body is None:
        return ""

    lines: List[str] = []

    for child in list(body):
        local = child.tag.rsplit("}", 1)[-1]
        if local == "para":
            text = text_from_node(child).replace("\u00a0", " ").rstrip()
            indent = child.find("n:styles/n:text-indent", XML_NS)
            level = int(indent.text) if indent is not None and indent.text and indent.text.isdigit() else 0
            if text:
                prefix = "    " * level
                lines.append(f"{prefix}{text}")
                lines.append("")
            else:
                append_blank(lines)
        elif local == "code":
            code = text_from_node(child).rstrip("\n")
            language = text_from_node(child, "language").strip()
            if language == "plain_text":
                language = ""
            lines.append(f"```{language}")
            lines.extend(code.splitlines())
            lines.append("```")
            lines.append("")
        elif local == "image":
            source = text_from_node(child, "source").strip()
            if source:
                local_path = store.download_image(source)
                lines.append(f"![]({local_path})")
                lines.append("")
        elif local == "attach":
            resource = text_from_node(child, "resource").strip() or text_from_node(child, "source").strip()
            filename = text_from_node(child, "filename").strip() or "attachment"
            if resource:
                local_path = store.download_attachment(resource, filename)
                lines.append(f"[{filename}]({local_path})")
                lines.append("")

    return normalize_markdown("\n".join(lines))


def new_json_to_markdown(content: str, store: ResourceStore) -> str:
    data = json.loads(content)
    blocks = data.get("5", [])
    lines: List[str] = []

    for block in blocks:
        block_type = block.get("6")
        meta = block.get("4") or {}

        if block_type == "im":
            url = meta.get("u")
            if url:
                local_path = store.download_image(url)
                lines.append(f"![]({local_path})")
                lines.append("")
            continue

        if block_type == "a":
            resource = meta.get("sr") or meta.get("re")
            filename = meta.get("fn") or "attachment"
            if resource:
                local_path = store.download_attachment(resource, filename)
                lines.append(f"[{filename}]({local_path})")
                lines.append("")
            continue

        if block_type == "cd":
            language = meta.get("la", "")
            code_lines = [extract_text(item) for item in block.get("5", [])]
            code = "\n".join(line.rstrip("\n") for line in code_lines).rstrip()
            lines.append(f"```{language}")
            if code:
                lines.extend(code.splitlines())
            lines.append("```")
            lines.append("")
            continue

        text = extract_text(block).rstrip()
        if text:
            indent = 0
            styles = meta.get("s") if isinstance(meta, dict) else None
            if isinstance(styles, dict) and isinstance(styles.get("ti"), int):
                indent = max(0, styles.get("ti", 0) // 28)
            lines.append(("    " * indent) + text)
            lines.append("")
        else:
            append_blank(lines)

    return normalize_markdown("\n".join(lines))


def extract_text(node: Any) -> str:
    if isinstance(node, dict):
        pieces: List[str] = []
        if "8" in node:
            pieces.append(str(node["8"]))
        for key in ("5", "7"):
            value = node.get(key)
            if isinstance(value, list):
                pieces.extend(extract_text(item) for item in value)
        return "".join(pieces)
    if isinstance(node, list):
        return "".join(extract_text(item) for item in node)
    return ""


def append_blank(lines: List[str]) -> None:
    if lines and lines[-1] != "":
        lines.append("")


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_content(payload: Dict[str, Any], store: ResourceStore) -> str:
    content = payload.get("content", "")
    if not isinstance(content, str) or not content.strip():
        return ""
    stripped = content.lstrip()
    if stripped.startswith("<"):
        return xml_to_markdown(content, store)
    if stripped.startswith("{"):
        return new_json_to_markdown(content, store)
    return normalize_markdown(content)


def split_post(raw: str) -> Tuple[str, str]:
    match = FRONT_MATTER_RE.match(raw)
    if not match:
        raise SyncError("Post has no front matter")
    return match.group(1), match.group(2)


def compose_body(target: NoteTarget, existing_body: str, note_md: str, note_title: str) -> str:
    body = existing_body.strip()

    if target.post_file == "hei-ping-guo.md":
        replacement = f"## {note_title}\n\n{note_md.strip()}\n"
        link = f"[在虚拟机上安装详细教程]({target.url})"
        if link in body:
            body = body.replace(link, replacement.strip())
        else:
            heading = f"\n## {note_title}"
            index = body.find(heading)
            if index >= 0:
                body = body[:index].rstrip() + "\n\n" + replacement.strip()
            else:
                body = body + "\n\n" + replacement.strip()
        return normalize_markdown(body)

    return note_md


def sync_target(target: NoteTarget, *, dry_run: bool = False) -> Dict[str, Any]:
    post_path = POSTS_DIR / target.post_file
    raw = post_path.read_text(encoding="utf-8")
    front_matter, old_body = split_post(raw)
    share_key = resolve_share_key(target.url)
    meta, payload = fetch_note_payload(share_key)
    store = ResourceStore(target.slug, dry_run=dry_run)
    note_md = convert_content(payload, store)
    note_title = str(payload.get("tl") or payload.get("title") or meta.get("fileMeta", {}).get("title") or "")
    new_body = compose_body(target, old_body, note_md, note_title)
    new_raw = front_matter.rstrip() + "\n\n" + new_body

    if not dry_run:
        post_path.write_text(new_raw, encoding="utf-8")

    return {
        "post": target.post_file,
        "share_key": share_key,
        "title": note_title,
        "markdown_chars": len(note_md),
        "resources": store.downloaded,
        "skipped": store.skipped,
        "changed": raw != new_raw,
    }


def update_posts_json() -> bool:
    if not POSTS_JSON.exists():
        return False
    data = json.loads(POSTS_JSON.read_text(encoding="utf-8"))
    posts = data.get("posts", [])
    by_name = {Path(t.post_file).stem: POSTS_DIR / t.post_file for t in TARGETS}
    changed = False

    for post in posts:
        file_name = post.get("fileName")
        path = by_name.get(file_name)
        if not path or not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        _, body = split_post(raw)
        body = body.strip()
        if post.get("content") != body:
            post["content"] = body
            changed = True

    if changed:
        with POSTS_JSON.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(data, ensure_ascii=False, indent=2))
            fh.write("\n")
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Fetch and convert without writing files.")
    parser.add_argument("--update-posts-json", action="store_true", help="Sync config/posts.json content cache.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results: List[Dict[str, Any]] = []

    for target in TARGETS:
        try:
            result = sync_target(target, dry_run=args.dry_run)
            results.append(result)
            print(
                f"OK {result['post']}: title={result['title']!r}, "
                f"chars={result['markdown_chars']}, resources={len(result['resources'])}, "
                f"skipped={len(result['skipped'])}, changed={result['changed']}"
            )
        except Exception as exc:
            print(f"ERROR {target.post_file}: {exc}", file=sys.stderr)
            return 1
        time.sleep(0.2)

    if args.update_posts_json and not args.dry_run:
        changed = update_posts_json()
        print(f"config/posts.json changed={changed}")

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
