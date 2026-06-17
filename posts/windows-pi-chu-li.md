---
id: uScrjg
title: windows批处理
createdAt: "2020-08-26 10:33:42"
updated: "2026-06-16 17:26:22"
tags:
    - Windows
    - Bat
tag_ids:
    - BhRpLA
    - pQW03i
categories:
    - 工具链
published: true
hideInList: false
feature: ""
isTop: false
---

- 1，批量处理删除文件
```
del /f /s /q *.meta
pause
```
- 2，批量修改图片名字
```@echo off
setlocal enabledelayedexpansion
set count=100
for /f "delims=" %%i in ('dir /b *.jpg,*.png,*.bmp,*.jpeg,*.gif') do call:Rename "%%~i"
pause
exit
 
:Rename
set /a count+=1
if /i "%~1"=="!count:~1!%~x1" goto :eof
if exist "!count:~1!%~x1" goto Rename
echo 改名：%1 !count:~1!
ren "%~1" "!count:~1!%~x1"
goto :eof


文件命名 .bat结尾
```
- 3，LayaAI obj convertTo Json
```
REM Author JUN_Z
REM Time 2020/8/26/14:16:57
@echo off    
setlocal enabledelayedexpansion
for %%i in ( *.obj ) do (
    set "FILE_NAME=%%~ni"
    echo "fileName": !FILE_NAME!
    call:runConvert %%~i,!FILE_NAME!
    )
pause

:runConvert
REM echo %1
REM echo %2%JSON%
start python convert_obj_three.py -i %1 -o %2.json
goto :eof
```