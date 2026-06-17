---
id: SEom4K
title: Jenkins-Unity-Android/iOS打包自动化
createdAt: "2025-07-22 11:08:06"
updated: "2026-06-17 10:10:59"
tags:
    - Unity
    - Android
    - iOS
    - 构建发布
tag_ids:
    - FjODty
    - SWem6w
    - UfqFAF
    - xn5J0z
categories:
    - 工具链
category_ids:
    - VFyF1L
published: true
hideInList: false
feature: ""
isTop: false
---

## CI（Continuous Integration，持续集成）
     * 每次提交都会触发自动化流程：编译 → 测试 → 静态检查
## CD（Continuous Delivery / Continuous Deployment，持续交付/部署）
    *  每次 CI 成功后，自动将构建产物（如 APK、Docker 镜像）部署到测试环境或预生产环境。
## Jenkins 初始化及配置
    * 配置未被占用端口及配置防火墙端口
    * 插件
        + Pipeline 可视化流水线
        + Hidden Parameter 参数隐藏
        + Persistent Parameter 参数持久化
        + Active Choices
    * Jenkins 权限
        * Jenkins服务中使用管理员账号密码登录并重启服务
    * 参数 
        + 仅在pipelineScript中新增的参数，会在下次构建时生成，会导致构建失败，可在 ``This project is parameterized?`` 中手动增加
        + 无需更改的参数应设置为 Hidden
## JenkinsFile
  ```
  pipeline {
    agent any

    parameters {
        // 用户可修改的持久化参数（版本号、是否构建 APK/AAB、是否同步 Git 等）
        persistentString(name: 'VERSION_NAME', defaultValue: '1.0.0', description: '应用版本号')
        .......
        // 隐藏参数（路径、签名、Webhook 等）
        hidden(name: 'UNITY_EDITOR_PATH', defaultValue: 'C:\\Program Files\\Unity\\Editor\\Unity.exe', description: 'Unity 编辑器路径')
        ......
    }

    environment {
        BUILD_OUTPUT_PATH = "D:\\Jenkins_IIS_Server\\${JOB_BASE_NAME}\\BuildOutput\\V${VERSION_CODE}\\"
        UNITY_LOG_PATH = "D:\\Jenkins_IIS_Server\\${JOB_BASE_NAME}\\UnityLog\\V${VERSION_CODE}\\"
        JENKINS_SERVER = "http://192.168.18.222:8085/"
        IIS_SERVER = "http://192.168.18.222:8086/"
    }

    stages {

        stage('Notify Build Start') {
            steps {
                script {
                    // 打印构建参数并发送飞书通知
                    echo "构建开始，发送飞书通知..."
                }
            }
        }

        stage('Check Environment') {
            steps {
                script {
                    // 检查 Unity、Gradle、签名文件等环境依赖
                    echo "检查环境依赖..."
                }
            }
        }
       ......

    post {
        success {
            script {
                // 构建成功通知，包含耗时和可下载文件
                echo "构建成功，发送飞书通知..."
            }
        }
        failure {
            script {
                // 构建失败通知，包含耗时和控制台日志链接
                echo "构建失败，发送飞书通知..."
            }
        }
    }
  ```
## UnityCode 
  ```
  Step1 
  自动构建调用静态方法 方法直至构建结束不应有   bool goon = EditorUtility.DisplayDialog("打包平台为安卓", "输出路径为：\n" + outPutPath, "继续", "取消"); 类似阻塞逻辑
  Step2
  自动构建 结束应该调用 EditorApplication.Exit(0); //失败则应是 -1 或者其他不为0 的Code,参考Cmd 返回码
  ```
  构建中如遇Unity编辑器重新编译（如果构建AB 生成新文件并调用AssetData.Refresh,此时异步打包方法会退出并无处调用 EditorApplication.Exit(0)），会导致Unity异步构建中断，不再会调用 ``EditorApplication.Exit(0); ``此时需要特殊处理
  超过一个小时，Jenkins 将强制打包失败 ，可通过 ``    timeout(time: 60, unit: 'MINUTES') `` 进行设置timeout
  建议解决方案，可控步骤都有抽成同步方法并Jenkins中配置对应stage
## AndroidCode
  ```
//适配Jenkins 自动命名
def versionCodeProp = project.hasProperty('versionCode') ? project.versionCode.toInteger() : 100
def versionNameProp = project.hasProperty('versionName') ? project.versionName : '1.0.0'
versionCode versionCodeProp
versionName versionNameProp
// 自动命名：Jenkins 传入 customName 优先，否则用默认  请勿修改
def baseName = project.hasProperty('customName') ? project.cu
setProperty("archivesBaseName", baseName)

// 自动命名：Jenkins 传入 customName 优先，否则用默认  请勿修改
android.applicationVariants.all { variant ->
    variant.outputs.all { output ->
        def baseName = project.hasProperty('customName') ? project.c
        // 判断是否 AAB / APK
        def isAAB
        def isAPK
        if (project.hasProperty('customName')) {
            // customName 存在时，通过名字中是否含 "_AAB_" 判断
            isAAB = baseName.contains("_AAB_")
            isAPK = !isAAB
        } else {
            // 没有 customName 时，使用传统方法判断
            isAAB = variant.name.toLowerCase().contains("bundle")
            isAPK = variant.name.toLowerCase().contains("assemble")
        }
        // 生成输出文件名
        def fileName = ""
        if (isAAB) {
            fileName = "${baseName}.aab"
        } else if (isAPK) {
            fileName = "${baseName}.apk"
        } else {
            fileName = "${baseName}.bin" // 兜底方案
        }
        output.outputFileName = fileName
    }
}

//获取时间，添加到发布版本中
static def releaseTime() {
    return new Date().format("yyyy-MM-dd-HH-mm", TimeZone.getTimeZone("GMT+08:00"))
}
```
## Android 构建环境
    * 不同Unity版本对应 Gradle版本不同，建议创建空项目，导出确认默认Android配置
## IIS 配置
    - 配置未被占用端口及配置防火墙端口
    - 配置目录浏览
    - 配置文件可下载
    - MIME类型配置支持 APK/AAB 文件下载