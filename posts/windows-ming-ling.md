---
title: 'Windows 命令'
date: 2025-07-22 16:59:44
tags: [Windows]
published: true
hideInList: false
feature: 
isTop: false
---
- echo (类似log) echo on / echo off  @echo @后面的命令不显示
- cd (path) 切换到path目录 cd.. 返回上一级目录
- dir 显示当前目录中的子文件夹和文件  dir /b 
- tree 当前文件下目录结构
- ren 重命名莫个文件/文件夹 
- md 创建目录
- rd 删除目录    /s/q(包括自目录和子文件)  /s 删除子文件夹 /q 不询问删除
- copy 复制文件 
- xcopy  /s 复制文件夹(递归复制)
- move 移动文件
- del 删除文件 不会删除目录及子目录
- replace 替换文件
- bat窗口
```
@echo off
title测试bat
color 03
mode con cols=50 lines=100
pause
```
- 文件写入内容
```
@echo off
title测试bat
color 03
mode con cols=80 lines=50
e:
cd e:\Work
echobat测试命令>>测试2.txt
pause 
```
- call 调用其他bat
- start 启动一个程序
- choice
```
@echo off
choice /c ync /m "确认Y,否N，取消C."  （/m代表显示的信息）
if errorlevel 3 goto C
if errorlevel 2 goto N
if errorlevel 1 goto Y

:Y
echo 确定
goto C

:N
echo 否
goto C

:C
echo 取消
pause
```
- for
```
cmd窗口里： for %i in (command1) do command2  (引用变量为%i)
在bat中： for %%i in (command1) do command2    (引用变量为%%i)
在command1 命令里面切分元素的时候，使用空格，逗号，等号作为分隔符
示例1：
cmd窗口里：  for %i in (abc) do echo %i
在bat中：for %%i in (a b,c) do echo %%i

/L 开关控制循环次数
for /L %i in (start,step,end) do command2   (start开始的i,step递增值，end结束值)
示例2：
for /l %i in (1,2,10) do echo %i
	
            
/F  delims=;   （每一行以;为分隔符）  
for /f "delims=;" %%i in (学习笔记.txt) do echo %%i

tokens=2 代表取每一行的第几列  tokens=1，2（取第一列和第二列） tokens = *（取全部）
for /f "tokens=1,* delims= " %%i in (学习笔记.txt) do echo %%i %%j

skip = 2 忽略前几行
for /f "skip=2 tokens=* delims= " %%i in (学习笔记.txt) do echo %%i

eol  忽略以什么字符开始的那一行
for /f "eol=f skip=2 tokens=* delims= " %%i in (学习笔记.txt) do echo %%i

usebackq （反转） for %%i in (command1) do command2   
for /f "usebackq tokens=* delims= " %%i in ("学习笔记.txt") do echo %%i
for /f "usebackq tokens=* delims= " %%i in ('echo siki学院') do echo %%i

```