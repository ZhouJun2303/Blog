---
id: FuiAlZ
title: Android 原生加密Jar工具包制作
createdAt: "2024-09-30 11:26:54"
updated: "2026-06-17 10:10:59"
tags:
    - Java
    - Jar
tag_ids:
    - irFZ9L
    - Qh55SV
categories:
    - 安全与逆向
category_ids:
    - 35S97K
published: true
hideInList: false
feature: ""
isTop: false
---

## 设计
- 设计思路
  可读接口->不可读接口
- Android 创建一个新的Lib
目录结构
```
--src
    --main
        --java com.tool.hwtools
            --CheckRoot
            --Hw.Tools
            --SignatureUtil
    --proguard-rules.pro
```
## 未加密代码
```
package com.tool.hwtools;

import android.content.Context;
import android.content.pm.Signature;

public class HwTools {
    public static boolean CachedValue = false;

    public static boolean IsDeviceRooted() {
        CachedValue = CheckRoot.isDeviceRooted();
        return CheckRoot.isDeviceRooted();
    }

    public static String getSignatureInfo256(Context context, String packageName) {
        return SignatureUtil.getSignatureInfo256(context, packageName);
    }

    public static String getSignatureInfo1(Context context, String packageName) {
        return SignatureUtil.getSignatureInfo1(context, packageName);
    }

    public static String getSignatureInfo256(Signature[] signatures) {
        return SignatureUtil.getSignatureInfo256(signatures);
    }

    public static String getSignatureInfo1(Signature[] signatures) {
        return SignatureUtil.getSignatureInfo1(signatures);
    }

    public static String getApkHash(Context context, String packageName) {
        return SignatureUtil.getApkHash(context, packageName);
    }
}

```
```
package com.tool.hwtools;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

import android.util.Log;


public class CheckRoot {
    // 定义TAG常量
    private static String TAG = CheckRoot.class.getName();

    public static boolean isDeviceRooted() {
        if (checkDeviceDebuggable()) {
            return true;
        }//check buildTags
        if (checkSuperuserApk()) {
            return true;
        }//Superuser.apk
        if (checkRootPathSU()) {
            return true;
        }//find su in some path
        if (checkRootWhichSU()) {
            return true;
        }//find su use 'which'
        if (checkBusybox()) {
            return true;
        }//find su use 'which'
        if (checkAccessRootData()) {
            return true;
        }//find su use 'which'
        if (checkGetRootAuth()) {
            return true;
        }//exec su

        return false;
    }


    // 检查判断是否存在SuperSU.apk文件，存在的话就是root
    private static boolean checkSuperuserApk() {
        try {
            File file = new File("/system/app/SuperSU/SuperSU.apk");
            if (file.exists()) {
                Log.w(TAG, "/system/app/SuperSU/SuperSU.apk exist");
                return true;
            }
        } catch (Exception e) {
        }
        return false;
    }


    private static boolean checkDeviceDebuggable() {
        String buildTags = android.os.Build.TAGS;
        if (buildTags != null && buildTags.contains("test-keys")) {
            Log.i(TAG, "buildTags=" + buildTags);
            return true;
        }
        return false;
    }

    private static boolean checkRootPathSU() {
        File f = null;
        final String kSuSearchPaths[] = {"/system/bin/", "/system/xbin/", "/system/sbin/", "/sbin/", "/vendor/bin/"};
        try {
            for (int i = 0; i < kSuSearchPaths.length; i++) {
                f = new File(kSuSearchPaths[i] + "su");
                if (f != null && f.exists()) {
                    Log.i(TAG, "find su in : " + kSuSearchPaths[i]);
                    return true;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    private static boolean checkRootWhichSU() {
        String[] strCmd = new String[]{"/system/xbin/which", "su"};
        ArrayList<String> execResult = executeCommand(strCmd);
        if (execResult != null) {
            Log.i(TAG, "execResult=" + execResult.toString());
            return true;
        } else {
            Log.i(TAG, "execResult=null");
            return false;
        }
    }

    private static ArrayList<String> executeCommand(String[] shellCmd) {
        String line = null;
        ArrayList<String> fullResponse = new ArrayList<String>();
        Process localProcess = null;
        try {
            Log.i(TAG, "to shell exec which for find su :");
            localProcess = Runtime.getRuntime().exec(shellCmd);
        } catch (Exception e) {
            return null;
        }
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(localProcess.getOutputStream()));
        BufferedReader in = new BufferedReader(new InputStreamReader(localProcess.getInputStream()));
        try {
            while ((line = in.readLine()) != null) {
                Log.i(TAG, "–> Line received: " + line);
                fullResponse.add(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        Log.i(TAG, "–> Full response was: " + fullResponse);
        return fullResponse;
    }

    private static synchronized boolean checkGetRootAuth() {
        Process process = null;
        DataOutputStream os = null;
        try {
            Log.i(TAG, "to exec su");
            process = Runtime.getRuntime().exec("su");
            os = new DataOutputStream(process.getOutputStream());
            os.writeBytes("exit\n");
            os.flush();
            int exitValue = process.waitFor();
            Log.i(TAG, "exitValue=" + exitValue);
            if (exitValue == 0) {
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            Log.i(TAG, "Unexpected error - Here is what I know: "
                    + e.getMessage());
            return false;
        } finally {
            try {
                if (os != null) {
                    os.close();
                }
                process.destroy();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private static synchronized boolean checkBusybox() {
        try {
            Log.i(TAG, "to exec busybox df");
            String[] strCmd = new String[]{"busybox", "df"};
            ArrayList<String> execResult = executeCommand(strCmd);
            if (execResult != null) {
                Log.i(TAG, "execResult=" + execResult.toString());
                return true;
            } else {
                Log.i(TAG, "execResult=null");
                return false;
            }
        } catch (Exception e) {
            Log.i(TAG, "Unexpected error - Here is what I know: "
                    + e.getMessage());
            return false;
        }
    }

    private static synchronized boolean checkAccessRootData() {
        try {
            Log.i(TAG, "to write /data");
            String fileContent = "test_ok";
            Boolean writeFlag = writeFile("/data/su_test", fileContent);
            if (writeFlag) {
                Log.i(TAG, "write ok");
            } else {
                Log.i(TAG, "write failed");
            }

            Log.i(TAG, "to read /data");
            String strRead = readFile("/data/su_test");
            Log.i(TAG, "strRead=" + strRead);
            if (fileContent.equals(strRead)) {
                return true;
            } else {
                return false;
            }
        } catch (Exception e) {
            Log.i(TAG, "Unexpected error - Here is what I know: "
                    + e.getMessage());
            return false;
        }
    }

    //写文件
    private static Boolean writeFile(String fileName, String message) {
        try {
            FileOutputStream fout = new FileOutputStream(fileName);
            byte[] bytes = message.getBytes();
            fout.write(bytes);
            fout.close();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    //读文件
    private static String readFile(String fileName) {
        File file = new File(fileName);
        try {
            FileInputStream fis = new FileInputStream(file);
            byte[] bytes = new byte[1024];
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            int len;
            while ((len = fis.read(bytes)) > 0) {
                bos.write(bytes, 0, len);
            }
            String result = new String(bos.toByteArray());
            Log.i(TAG, result);
            return result;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```
```
package com.tool.hwtools;


import android.content.Context;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.Signature;
import android.util.Log;

import java.io.FileInputStream;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SignatureUtil {
    private static final String TAG = "SignatureUtil";

    public static String getSignatureInfo256(Context context, String packageName) {
        try {
            PackageInfo packageInfo = context.getPackageManager().getPackageInfo(packageName, PackageManager.GET_SIGNATURES);
           return getSignatureInfo256(packageInfo.signatures);
        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static String getSignatureInfo1(Context context, String packageName) {
        try {
            PackageInfo packageInfo = context.getPackageManager().getPackageInfo(packageName, PackageManager.GET_SIGNATURES);
            return getSignatureInfo1(packageInfo.signatures);
        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static String getSignatureInfo256(Signature[] signatures) {
        if (null == signatures) return "Null";
        StringBuilder sb = new StringBuilder();
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            for (Signature signature : signatures) {
                byte[] signatureBytes = signature.toByteArray();
                byte[] hashBytes = md.digest(signatureBytes);
                String hash = bytesToHex(hashBytes);
                sb.append("Signature Hash 256: ").append(hash).append("\n\n");
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    public static String getSignatureInfo1(Signature[] signatures) {
        if (null == signatures) return "Null";
        StringBuilder sb = new StringBuilder();
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-1");
            for (Signature signature : signatures) {
                byte[] signatureBytes = signature.toByteArray();
                byte[] hashBytes = md.digest(signatureBytes);
                String hash = bytesToHex(hashBytes);
                sb.append("Signature Hash 1: ").append(hash).append("\n\n");
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x:", b));
        }
        // 删除最后一个冒号
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }

    public static String getApkHash(Context context, String packageName) {
        try {
            PackageInfo packageInfo = context.getPackageManager().getPackageInfo(packageName, PackageManager.GET_SIGNATURES);
            String apkFilePath = packageInfo.applicationInfo.sourceDir;
            return calculateHash(apkFilePath);
        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        } catch (IOException | NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    private static String calculateHash(String filePath) throws IOException, NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        try (FileInputStream fis = new FileInputStream(filePath)) {
            byte[] buffer = new byte[8192];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                md.update(buffer, 0, bytesRead);
            }
        }
        byte[] hashBytes = md.digest();
        StringBuilder sb = new StringBuilder();
        for (byte hashByte : hashBytes) {
            sb.append(Integer.toString((hashByte & 0xff) + 0x100, 16).substring(1));
        }
        return sb.toString();
    }

    public static String convertFormattedHashToHex(String formattedHash) {
        // 去除冒号
        // formattedHash = formattedHash.replaceAll(":", "");

        // 转换为十六进制表示
        StringBuilder hexHash = new StringBuilder();
        for (int i = 0; i < formattedHash.length(); i += 2) {
            String hexByte = formattedHash.substring(i, i + 2);
            int decimal = Integer.parseInt(hexByte, 16);
            String hex = Integer.toHexString(decimal);
            hexHash.append(hex);
        }

        return hexHash.toString();
    }

}
```

```
# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Uncomment this to preserve the line number information for
# debugging stack traces.
#-keepattributes SourceFile,LineNumberTable

# If you keep the line number information, uncomment this to
# hide the original source file name.
#-renamesourcefileattribute SourceFile
-keep class com.tool.hwtools.HwTools {
    *;
}

-keepnames class com.tool.hwtools.HwTools {
    *;
}
```
## Jar生成位置
```
build/.transforms..../out/jars/classes.jar
```