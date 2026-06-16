---
title: 'NodeJS连接数据库'
date: 2019-07-03 10:06:59
tags: [NodeJS,MySql]
published: true
hideInList: false
feature: 
isTop: false
---
- 安装mysql模块
```
npm install mysql
```
- 创建表时的组装
```
 let sql = `CREATE TABLE \`${config.database}\` .\`userinfo_qsz\`(
                \`uniqueID\` INT NOT NULL,
                \`accountID\` VARCHAR(45) NULL,
                \`password\` VARCHAR(45) NULL,
                \`nickName\` VARCHAR(45) NULL,
                PRIMARY KEY (\`uniqueID\`))
                ENGINE = InnoDB
                DEFAULT CHARACTER SET = utf8;`
```
```
"CREATE TABLE USERINFO_FOR_QSZ(
      uniqueID INT UNSIGNED NOT NULL AUTO_INCREMENT,
      accountID VARCHAR(45)  NULL,
      password VARCHAR(45)  NULL,
      nickName VARCHAR(45)  NULL,
)ENGINE = INNODB DEFAULT CHARSET = UTF8;"
```
- 用户数据表的创建
```
CREATE TABLE `tank_07_05`.`userinfo_tank` (
  `uniqueID` INT NOT NULL AUTO_INCREMENT,
  `accountID` VARCHAR(45) NOT NULL,
  `nickName` VARCHAR(45) NULL,
  `avatarURL` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`uniqueID`, `accountID`));
```