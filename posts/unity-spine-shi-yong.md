---
id: 5KcprI
title: Unity Spine 使用
createdAt: "2023-07-06 18:45:10"
updated: "2026-06-17 10:11:00"
tags:
    - Spine
tag_ids:
    - YR4Yni
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

## [融合动画](https://zhoujun2303.github.io/post/unity-spine-rong-he-dong-hua/)
## 皮肤切换 附件挂点切换
- GetNewAttachment 获取一个新的附件
```
//获取 Sprite资源
 Sprite attachmentSprite = LoaderCtrl.LoadSprite(iconResPath);
 //替换原附件图片，并拷贝新的附件
 var newAttachment = oldAttachment.GetRemappedClone(attachmentSprite, oldAttachment.GetMaterial());
```
- SkeletonAnimation的切换（3D）
```
原理，并非可直接使用
//提取默认皮肤
Skeleton activatedSkeleton = skeletonAnimation.Skeleton;
activatedSkeleton.SetSkin("skin1");
Spine.Skin activatedSkin = activatedSkeleton.Data.FindSkin("skin1");
//克隆皮肤数据
Spine.Skin collectedSkin = new Spine.Skin("CollectedSkin");
activatedSkin.CopyTo(collectedSkin, true, true, true);
//根据 挂点名字查找附件下标
int slotIndex = activatedSkeleton.FindSlotIndex(slotName);
string attachmentName = PathSpineBone.SoldierSlotToAttachmentMap[slotName];
//此处的坑 如果角色存在多个皮肤，在部分皮肤上没有附件打孔，那么此时的oldAttachment获取可能为 null
Attachment oldAttachment = skeletonAnimation.Skeleton.GetAttachment(slotIndex, attachmentName);
//将图片转为附件
string attachmentSpriteResPath = PathSpineBone.SoldierSlotToTextureDirMap[slotName] + iconName;
//克隆一个新的附件
var newAttachment = SpineCtrl.GetNewAttachment(oldAttachment, attachmentSpriteResPath);
//设置或者替换成新的附件 将莫个武器节点隐藏实际上就是赋值为 null
collectedSkin.SetAttachment(slotIndex, attachmentName, newAttachment);
//合并贴图，需要清理缓存
Material materialPropertySource = skeletonAnimation.SkeletonDataAsset.atlasAssets[0].PrimaryMaterial;//!!! 为了拷贝shader
CachedSpineSkinData cachedSkinData = new CachedSpineSkinData();
//生成一个新皮肤
cachedSkinData.skin = collectedSkin.GetRepackedSkin(dicKey, materialPropertySource, out cachedSkinData.material, out cachedSkinData.atlas, maxAtlasSize: 1024, clearCache: true);
activatedSkeleton.Skin = cachedSkinData.skin;

```
- SkeletonGraphic的切换 (UI)
```
大致原理 同上
var skeleton = skeletonGraphic.Skeleton;
Material sourceMaterial = skeletonGraphic.SkeletonDataAsset.atlasAssets[0].PrimaryMaterial;
Texture2D runtimeAtlas = null;
Material runtimeMaterial = null;

Skin customSkin = new Skin("custom skin");
skeletonGraphic.Skeleton.SetSkin("skin1");
var baseSkin = skeleton.Data.FindSkin("skin1");

int slotIndex = skeleton.FindSlotIndex(slotName);
Sprite attachmentSprite = LoaderCtrl.LoadSprite(PathSprite.Textures_clothes_common2_box_clear);
Attachment baseAttachment = skeleton.GetAttachment(slotIndex, slotName);
Attachment newAttachment = baseAttachment.GetRemappedClone(attachmentSprite, sourceMaterial);
customSkin.SetAttachment(slotIndex, slotName, newAttachment);

 var repackedSkin = new Skin("repacked skin");
 //此处有个坑，当一个附件没有打在所有的皮肤上时，贴图会混乱
 1，让美术给每个皮肤都打上附件
 2，实例化的新皮肤，将需要所有挂点都依次替换，既下列方式
 repackedSkin.AddAttachments(baseSkin);
 repackedSkin.AddAttachments(customSkin);
 repackedSkin = repackedSkin.GetRepackedSkin(dicKey, sourceMaterial, out runtimeMaterial, out runtimeAtlas, clearCache: true);
 CachedSpineSkinData cachedSpineSkinData = new CachedSpineSkinData();
 cachedSpineSkinData.skin = repackedSkin;
 cachedSpineSkinData.atlas = runtimeAtlas;

skeleton.SetSkin(repackedSkin);
skeleton.SetToSetupPose();
skeletonGraphic.Update(0);
//This is used by the UI system to determine what to put in the MaterialPropertyBlock.
skeletonGraphic.OverrideTexture = runtimeAtlas;
```