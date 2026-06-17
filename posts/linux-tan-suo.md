---
id: atrQWQ
title: Linux 探索
createdAt: "2020-07-22 11:26:27"
updated: "2026-06-16 17:26:22"
tags:
    - Linux
tag_ids:
    - J1aZtK
categories:
    - 工具链
published: true
hideInList: false
feature: ""
isTop: false
---

## 搭建
## node.js环境服务器
## 安装mysql
```
wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz
```
[nginx配置APK](https://www.cnblogs.com/yybrhr/p/11413035.html)
[参考链接](https://www.jianshu.com/p/276d59cbc529)

- linux配置图片
```
 location ~ .*\.(gif|jpg|jpeg|png)$ {  
            expires 24h;  
            root /home/pic/;#指定图片存放路径  
            access_log  /home/nginx/logs/images.log;#图片 日志路径  
            proxy_store on;  
        }
```
- linux配置文件夹浏览
```
 server {
        listen       9002;
        server_name  localhost;

        location ~ ^/(img|data|js|css|html|templates)/ {
            root  /Hot;
        }

        location ~ ^/customizedtraffic {
            fastcgi_pass   0.0.0.0:9091;
            fastcgi_param  QUERY_TYPE        traffic;
            include        fastcgi_params;
        }

        location ~ ^/agentserver {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://100.69.195.166:7143;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }


    server {
        listen       9002;
        server_name  localhost;

        location / {
            autoindex on;
            autoindex_exact_size off;
            root   /Hot;
        }
```

- nginx重启
```
cd /usr/local/nginx/sbin
./nginx -s reload
```
- pm2 常驻管理自动重启
```
重启所有： pm2 restart all 
 清楚日志 # pm2 flush              #Empty all log file
nginx
重启：./nginx  -s reload  //此命令在Sbin目录下执行
```
- lrzsz替代ftp上传和下载文件
```
// 首先安装lrzsz 
# yum -y install lrzsz 
// 上传文件，执行命令rz，会跳出文件选择窗口，选择好文件，点击确认即可。
# rz

// 下载文件，执行命令sz
# sz
```
```
空目录  opt  //主要操作目录
安装文件目录 mnt //安装应用程序
```
- 网页配置demo
```
server {
        listen       8889;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root  /webgame/web-mobile;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
```
