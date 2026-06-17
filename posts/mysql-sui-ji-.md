---
id: EuWrT1
title: MySql随记
createdAt: "2019-07-03 10:14:12"
updated: "2026-06-16 17:26:22"
tags:
    - MySql
tag_ids:
    - gRjAxH
categories:
    - 编程基础
published: true
hideInList: false
feature: ""
isTop: false
---

- 创建数据库
```
CREATE` SCHEMA `数据库名字` ;
```
```
-- show databases
-- 选择使用的数据库
use qsz_database_20190703;
-- 显示数据库下所有的表
show tables;
-- 查看表单结构
describe userinfo;
-- 向表中添加信息
-- insert into userinfo(uniqueID,accountID,passworld,nickName) values(2,2,3,"A");
-- insert into userinfo(uniqueID,accountID,passworld,nickName) values( 3,2,3,"B");
-- insert into userinfo(uniqueID,accountID,passworld,nickName) values( 5,2,3,"C");
-- 显示表单内容
-- select *from userinfo

SET SQL_SAFE_UPDATES = 0;
-- 删除玩家
delete from userinfo where  nickName="A";
-- 查找用户信息表
-- select *from userinfo;

-- 查找用户信息
select *from userinfo where nickName="B";
-- 修改指定用户的指定信息
-- 一次修改一个人，可以修改多个值
update  userinfo set passworld=6666,gameWon=10 where nickName="B";

-- 查找表
-- select *from userinfo_qsz;
-- 清空表
-- TRUNCATE TABLE userinfo_qsz;

-- 查找表是否存在
-- SELECT table_name FROM information_schema.TABLES WHERE table_name = "userinfo";
```
## 数据库的
![](/post-images/1659752245956.jpg)

- 创建数据表的操作指令
```
CREATE TABLE `qsz_database_20190703`.`userinfo` (
  `uniqueID` INT NOT NULL,
  `accountID` VARCHAR(45) NULL,
  `passworld` VARCHAR(45) NULL,
  `nickName` VARCHAR(45) NULL,
  `avatarURL` VARCHAR(45) NULL,
  `gameWon` INT UNSIGNED ZEROFILL NULL,
  `gameLost` INT UNSIGNED ZEROFILL NULL,
  PRIMARY KEY (`uniqueID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
```
[参考链接](https://www.jianshu.com/p/c8eb6d2471f8)

```
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;

 ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';  
```
```
CREATE TABLE `数据库名`.`表名`(
    
)
```
![](/post-images/1659752355662.jpg)
- 数据库的查询
![](/post-images/1659752379560.jpg)
```
show databases;
```
- 注释
```
--  空格
```
![](/post-images/1659752454143.jpg)

- 查看表单具体结构
![](/post-images/1659752471099.jpg)

- 表中添加 信息
![](/post-images/1659752504465.jpg)

- 非主键数据表数据删除
![](/post-images/1659752528723.jpg)
