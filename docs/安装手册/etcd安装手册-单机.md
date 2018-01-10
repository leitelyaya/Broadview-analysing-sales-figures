#  etcd安装手册-单机
## 1 etcd简介
etcd组件作为一个高可用、强一致性的服务发现存储仓库，渐渐为开发人员所关注。在云计算时代，如何让服务快速透明地接入到计算集群中，如何让共享配置信息快速被集群中的所有机器发现，更为重要的是，如何构建这样一套高可用、安全、易于部署以及响应快速的服务集群，已经成为了迫切需要解决的问题。etcd是一个键值存储仓库，于配置共享和服务发现。

etcd的特点：

- 简单：基于HTTP+JSON的API让你用curl命令就可以轻松使用。
- 安全：可选SSL客户认证机制。
- 快速：每个实例每秒支持一千次写操作。
- 可信：使用Raft算法充分实现了分布式。

### 1.1 场景一：服务发现

### 1.2 场景二：消息发布与订阅

### 1.3 场景三：负载均衡

### 1.4 场景四：分布式通知与协调

### 1.5 场景五：分布式锁

### 1.6 场景六：分布式队列

### 1.7 场景七：集群监控与Leader竞选


### 1.8 为什么用etcd而不用ZooKeeper？


## 2 安装etcd




### 2.1 RedHat安装


#### 2.1.1 安装Go
因为etcd是go语言编译，所以先要安装go环境，要求go1.9+，另外需要注意：

```
编译GO 1.6版本以上的需要依赖GO 1.4版本的二进制，并且需要把GOROOT_BOOTSTRAP的路径设置为1.4版本GO的根目录，这样它的bin目录就可以直接使用到1.4版本的GO
```


第一步：下载Go源程序到__“/usr/local/src”__

```powershell
 [root@iZ23m1dgviaZ local]# curl -O https://dl.google.com/go/go1.9.2.src.tar.gz
```
 
第二步：解压程序到__“/usr/local/src”__：


```powershell
[root@iZ23m1dgviaZ local]# tar -C /usr/local/src -xzf   go1.9.2.src.tar.gz
[root@iZ23m1dgviaZ local]# mv go go1.9.2
```


第三步：git下载Go源代码，并编译出如下所示：

```powershell
[root@iZ23m1dgviaZ local]# git clone git@github.com:golang/go.git
[root@iZ23m1dgviaZ local]# cd go
[root@iZ23m1dgviaZ local]# git checkout -b 1.4.3 go1.4.3
[root@iZ23m1dgviaZ local]# cd src
[root@iZ23m1dgviaZ local]# ./all.bash
#复制 /usr/local/src/go 到 /usr/local/go1.4
```

第四步：添加环境变量GOROOT_BOOTSTRAP：

```powershell
[root@iZ23m1dgviaZ local]# export GOROOT_BOOTSTRAP=/usr/local/go1.4
```

第五步：进入/usr/local/src/go 编译出1.9.2版本

```powershell
[root@iZ23m1dgviaZ local]# git clean -dfx
[root@iZ23m1dgviaZ local]# git checkout -b 1.9.2 go1.9.2
[root@iZ23m1dgviaZ local]# cd src
[root@iZ23m1dgviaZ local]# ./all.bash
#等待编译完成
```

第六步：设置go的环境变量：

```powershell
[root@iZ23m1dgviaZ local]# export GOROOT=/usr/local/go
[root@iZ23m1dgviaZ local]# export PATH=$PATH:$GOROOT/bin
[root@iZ23m1dgviaZ local]# go version
go version go1.9.2 linux/386
```

第七步：编写helloworld，进行测试：

创建一个/usr/local/src/hello/hello.go，内容如下所示：

```go
package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
}
```

编译和运行hello.go语言：

```powershell
[root@iZ23m1dgviaZ hello]# go build hello.go
[root@iZ23m1dgviaZ hello]# ls
hello  hello.go
[root@iZ23m1dgviaZ hello]# ./hello 
hello, world
```

第八步：至此go1.9.2的环境已经搭建完成，将上面用到的环境变量添加到/etc/profile中：

```profile
#add go path
export GOROOT_BOOTSTRAP=/usr/local/go1.4
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
```
并source profile，如下所示：

```powershell
[root@iZ23m1dgviaZ hello]# source /etc/profile
```

#### 2.1.2 安装etcd
go的环境搭建好了以后，接下来可以下载etcd，然后进行源码安装编译了。


第一步：下载etcd到__“/usr/local/src”__

```powershell
[root@iZ23m1dgviaZ src]#  git clone https://github.com/coreos/etcd.git
Initialized empty Git repository in /usr/local/src/etcd/.git/
remote: Counting objects: 70808, done.
remote: Compressing objects: 100% (97/97), done.
remote: Total 70808 (delta 33), reused 45 (delta 17), pack-reused 70694
Receiving objects: 100% (70808/70808), 34.77 MiB | 4.64 MiB/s, done.
Resolving deltas: 100% (44465/44465), done.
```

第二步：编译并运行etcd，如下所示：

```powershell
[root@iZ23m1dgviaZ src]# cd etcd/
[root@iZ23m1dgviaZ etcd]# ./build
[root@iZ23m1dgviaZ etcd]#  ./bin/etcd
2018-01-10 10:34:10.336363 E | etcdmain: etcd on unsupported platform without ETCD_UNSUPPORTED_ARCH=386 set.
```

如上所示启动时出现了错误，配置环境变量：

```powershell
[root@iZ23m1dgviaZ etcd]#  export ETCD_UNSUPPORTED_ARCH=386
```

再启动etcd，会出现如下所示：

```
[root@iZ23m1dgviaZ etcd]#  ./bin/etcd
2018-01-10 10:34:10.336363 E | etcdmain: etcd on unsupported platform without ETCD_UNSUPPORTED_ARCH=386 set.
[root@iZ23m1dgviaZ etcd]# etcd on unsupported platform without ETCD_UNSUPPORTED_ARCH=386 set.^C
[root@iZ23m1dgviaZ etcd]# [root@iZ23m1dgviaZ etcd]#  ./bin/etcd
-bash: [root@iZ23m1dgviaZ: command not found
[root@iZ23m1dgviaZ etcd]# export ETCD_UNSUPPORTED_ARCH=386
[root@iZ23m1dgviaZ etcd]# ./bin/etcd
2018-01-10 10:42:07.243858 W | etcdmain: running etcd on unsupported architecture "386" since ETCD_UNSUPPORTED_ARCH is set
2018-01-10 10:42:07.244287 I | etcdmain: etcd Version: 3.3.0+git
2018-01-10 10:42:07.244302 I | etcdmain: Git SHA: 52f73c5
2018-01-10 10:42:07.244309 I | etcdmain: Go Version: go1.9.2
2018-01-10 10:42:07.244316 I | etcdmain: Go OS/Arch: linux/386
2018-01-10 10:42:07.244323 I | etcdmain: setting maximum number of CPUs to 1, total number of available CPUs is 1
2018-01-10 10:42:07.244337 W | etcdmain: no data-dir provided, using default data-dir ./default.etcd
2018-01-10 10:42:07.246006 I | embed: listening for peers on http://localhost:2380
2018-01-10 10:42:07.247160 I | embed: listening for client requests on localhost:2379
2018-01-10 10:42:07.256777 I | etcdserver: name = default
2018-01-10 10:42:07.256792 I | etcdserver: data dir = default.etcd
2018-01-10 10:42:07.256801 I | etcdserver: member dir = default.etcd/member
2018-01-10 10:42:07.256808 I | etcdserver: heartbeat = 100ms
2018-01-10 10:42:07.256815 I | etcdserver: election = 1000ms
2018-01-10 10:42:07.256821 I | etcdserver: snapshot count = 100000
2018-01-10 10:42:07.256834 I | etcdserver: advertise client URLs = http://localhost:2379
2018-01-10 10:42:07.256842 I | etcdserver: initial advertise peer URLs = http://localhost:2380
2018-01-10 10:42:07.256855 I | etcdserver: initial cluster = default=http://localhost:2380
2018-01-10 10:42:07.294469 I | etcdserver: starting member 8e9e05c52164694d in cluster cdf818194e3a8c32
2018-01-10 10:42:07.294514 I | raft: 8e9e05c52164694d became follower at term 0
2018-01-10 10:42:07.294532 I | raft: newRaft 8e9e05c52164694d [peers: [], term: 0, commit: 0, applied: 0, lastindex: 0, lastterm: 0]
2018-01-10 10:42:07.294542 I | raft: 8e9e05c52164694d became follower at term 1
2018-01-10 10:42:07.308313 W | auth: simple token is not cryptographically signed
```


第三步：另起一个终端，进行测试，如下所示，如果打印出 `hello wold`说明吗服务正常：

```powershell
[root@iZ23m1dgviaZ bin]# ./etcdctl set /foo/bar "hello world"
hello world
```

第四步：编写etcd启动脚本，建立软链接：

创建/usr/local/src/etcd/bin/etcd.sh，内容如下所示：

```shell
#!/bin/sh
echo 'start etcd...'
/usr/local/src/etcd/bin/etcd  & >/dev/null 2>&1
echo 'finished starting etcd.'
```

创建软链接，如下所示：

```powershell
ln -s /usr/local/src/etcd/bin/etcd.sh /usr/local/bin/etcd
ln -s /usr/local/src/etcd/bin/etcdctl /usr/local/bin/etcdctl
```

测试软链接：

```powershell
[root@iZ23m1dgviaZ local]# ps -ef|grep etcd
root     19643     1  0 10:54 pts/0    00:00:01 ./etcd
root     19696 19545  0 11:01 pts/1    00:00:00 grep etcd

[root@iZ23m1dgviaZ local]# kill -9 19643
[root@iZ23m1dgviaZ local]# ps -ef|grep etcd
root     19698 19545  0 11:02 pts/1    00:00:00 grep etcd

[root@iZ23m1dgviaZ local]# etcd

[root@iZ23m1dgviaZ local]# ps -ef|grep etcd
root     19714     1  0 11:04 pts/1    00:00:00 /usr/local/src/etcd/bin/etcd
root     19729 19545  0 11:05 pts/1    00:00:00 grep etcd


[root@iZ23m1dgviaZ ~]# etcdctl set /foo/bar "hello world"
hello world
```

第五步：将etcd需要用到的环境变量，配置到/etc/profile中，如下所示：

添加内容

```profile
#add etc path
export ETCD_UNSUPPORTED_ARCH=386
```

生效配置文件：

```powershell
 source /etc/profile
```


## 参考链接
__Go安装：__

http://blog.csdn.net/qq_15437667/article/details/59776840

__etcd安装参考：__

http://blog.csdn.net/chenjh213/article/details/53516949

__etcd介绍参考：__

http://www.infoq.com/cn/articles/etcd-interpretation-application-scenario-implement-principle