#  Supervisor安装手册

[TOC]

## 1 Supervisor简介

Supervisor（http://supervisord.org/）是用Python开发的一个client/server服务，是Linux/Unix系统下的一个进程管理工具，不支持Windows系统。它可以很方便的监听、启动、停止、重启一个或多个进程。用Supervisor管理的进程，当一个进程意外被杀死，supervisort监听到进程死后，会自动将它重新拉起，很方便的做到进程自动恢复的功能，不再需要自己写shell脚本来控制。

因为Supervisor是Python开发的，安装前先检查一下系统否安装了Python2.4以上版本。

## 2 Redhat安装

### 2.1 安装virtualenv
在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

```bash
pip3 install virtualenv
```


### 2.2 安装Python2
因为supervisor不支持python3，所以使用需要先安装python2

- 下载python 2.7.14

```bash
wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tar.xz
```

- 安装python 2.7.14

```bash
tar Jxvf Python-2.7.14.tar.xz
cd  Python-2.7.14
./configure --prefix=/usr/local/python2
make && make install
```

- 安装pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

- 建立软链接

```bash
ln -fs /usr/local/python2/bin/python2 /usr/bin/python2
ln -fs /usr/local/python2/bin/pip2.7 /usr/bin/pip2

```


### 2.3 安装supervisor

- 安装supervisor

```bash
pip2 install supervisor
ln -fs /usr/local/python2/bin/echo_supervisord_conf /usr/bin/echo_supervisord_conf
ln -fs /usr/local/python2/bin/supervisord /usr/bin/supervisord
ln -fs /usr/local/python2/bin/supervisorctl /usr/bin/supervisorctl
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```


- 配置基本启动参数：

```propertites
[unix_http_server]
file=/tmp/supervisor.sock   ;UNIX socket 文件，supervisorctl 会使用
;chmod=0700                 ;socket文件的mode，默认是0700
;chown=nobody:nogroup       ;socket文件的owner，格式：uid:gid

[inet_http_server]         ;HTTP服务器，提供web管理界面
port=*:8765        ;Web管理后台运行的IP和端口，如果开放到公网，需要注意安全性
username=user              ;登录管理后台的用户名
password=abc@123               ;登录管理后台的密码

[supervisord]
logfile=/home/data/logs/supervisord/supervisord.log ;日志文件，默认是 $CWD/supervisord.log
logfile_maxbytes=50MB        ;日志文件大小，超出会rotate，默认 50MB，如果设成0，表示不限制大小
logfile_backups=10           ;日志文件保留备份数量默认10，设为0表示不备份
loglevel=info                ;日志级别，默认info，其它: debug,warn,trace
pidfile=/tmp/supervisord.pid ;pid 文件
nodaemon=false               ;是否在前台启动，默认是false，即以 daemon 的方式启动
minfds=1024                  ;可以打开的文件描述符的最小值，默认 1024
minprocs=200                 ;可以打开的进程数的最小值，默认 200

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ;通过UNIX socket连接supervisord，路径与unix_http_server部分的file一致
;serverurl=http://127.0.0.1:9001 ; 通过HTTP的方式连接supervisord

;包含其它配置文件
[include]
files=/etc/supervisor/config.d/*.ini    ;可以指定一个或多个以.ini结束的配置文件
```

- 这里配置一个test-app.ini，如下所示：

```propertites
; [program:xx]是被管理的进程配置参数，xx是进程的名称
[program:test-app]
command=/usr/local/tomcat/test-app/bin/catalina.sh run  ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=tomcat          ; 用哪个用户启动进程，默认是root
priority=999         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/usr/local/tomcat/test-app/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程
```


- 启动supervisor

```bash
supervisord -c /etc/supervisor/supervisord.conf
```





