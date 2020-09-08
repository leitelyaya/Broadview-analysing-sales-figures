# 搭建ETCD
---
### 写在前面
    环境配置：go语言环境  git环境
---
## 环境搭建

#### 安装ETCD

<p>
<pre><code>

ETCD_VER=v3.3.0-rc.4

GOOGLE_URL=https://storage.googleapis.com/etcd

GITHUB_URL=https://github.com/coreos/etcd/releases/download

DOWNLOAD_URL=${GOOGLE_URL}

rm -f /usr/local/etcd-${ETCD_VER}-linux-amd64.tar.gz

rm -rf /usr/local/etcd && mkdir -p /usr/local/etcd

curl -L ${DOWNLOAD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o /usr/local/etcd-${ETCD_VER}-linux-amd64.tar.gz

tar xzvf /usr/local/etcd-${ETCD_VER}-linux-amd64.tar.gz -C /usr/local/etcd --strip-components=1

rm -f /usr/local/etcd-${ETCD_VER}-linux-amd64.tar.gz

</code></pre>
</p>

#### 查看安装结果

<p>
<pre><code>

/usr/local/etcd/etcd --version

ETCDCTL_API=3 /usr/local/etcd/etcdctl version

</code></pre>
</p>

#### 启动ETCD

<p>
<pre><code>

/usr/local/etcd/etcd

</code></pre>
</p>

#### 数据存储与获取

<p>
<pre><code>

ETCDCTL_API=3 /usr/local/etcd/etcdctl --endpoints=localhost:2379 put foo bar

ETCDCTL_API=3 /usr/local/etcd/etcdctl --endpoints=localhost:2379 get foo

</code></pre>
</p>

#### 本地集群
- 首先安装goreman
- `cd /usr/local/etcd && goreman start`  #集群配置为Procfile
- Procfile文件内容如下：

  `etcd1: bin/etcd --name infra1 --listen-client-urls http://127.0.0.1:2379 --advertise-client-urls http://127.0.0.1:2379 --listen-peer-urls http://127.0.0.1:12380 --initial-advertise-peer-urls http://127.0.0.1:12380 --initial-cluster-token etcd-cluster-1 --initial-cluster 'infra1=http://127.0.0.1:12380,infra2=http://127.0.0.1:22380,infra3=http://127.0.0.1:32380' --initial-cluster-state new --enable-pprof`
  
  `etcd2: bin/etcd --name infra2 --listen-client-urls http://127.0.0.1:22379 --advertise-client-urls http://127.0.0.1:22379 --listen-peer-urls http://127.0.0.1:22380 --initial-advertise-peer-urls http://127.0.0.1:22380 --initial-cluster-token etcd-cluster-1 --initial-cluster 'infra1=http://127.0.0.1:12380,infra2=http://127.0.0.1:22380,infra3=http://127.0.0.1:32380' --initial-cluster-state new --enable-pprof`
  
  `etcd3: bin/etcd --name infra3 --listen-client-urls http://127.0.0.1:32379 --advertise-client-urls http://127.0.0.1:32379 --listen-peer-urls http://127.0.0.1:32380 --initial-advertise-peer-urls http://127.0.0.1:32380 --initial-cluster-token etcd-cluster-1 --initial-cluster 'infra1=http://127.0.0.1:12380,infra2=http://127.0.0.1:22380,infra3=http://127.0.0.1:32380' --initial-cluster-state new --enable-pprof`
  
- 共三个members，分别监听2379、22379、32379端口。可用命令`etcdctl --write-out=table --endpoints=localhost:2379 member list`查看。
- kill某个member：`goreman run stop etcd2`
- restart该member：`goreman run restart etcd2`

#### 自我发现discovery
- 本地集群中配置文件使用了--initial-cluster参数，指明了集群中所有服务，一种静态方式。
- 实际项目中需要动态灵活的配置服务数量。etcd支持基于cluster的自我发现与完全自我发现。两种方式：etcd discovery和DNS discovery。以下以etcd discovery方式介绍：
  1. 基于已有集群动态发现
  
     假设已有的etcd集群的一个访问地址是：192.168.2.210，那么我们首先需要在已有etcd中创建一个特殊的key：
     `curl -X PUT https://192.168.2.210:2379/v2/keys/discovery/6c007a14875d53d9bf0ef5a6fc0257c817f0fb83/_config/size -d value=3`
     
     ps: 
        
         6c007a14875d53d9bf0ef5a6fc0257c817f0fb83为自己生成的id

         value=3表示集群大小
         
  2. 基于Public etcd discovery service
     
     通过etcd提供的服务生成key：

     `curl https://discovery.etcd.io/new?size=3`
     
     结果：`https://discovery.etcd.io/bb0e48ca0da0ec3e5aa5f7275835c60c`
     
  3. 将第一步或者第二步生成的自我发现url配置到Procfile中：
     
     `etcd --name infra0 --initial-advertise-peer-urls http://10.0.1.10:2380 \`

     `--listen-peer-urls http://10.0.1.10:2380 \`
     
     `--listen-client-urls http://10.0.1.10:2379,http://127.0.0.1:2379 \`
     
     `--advertise-client-urls http://10.0.1.10:2379 \`
     
     `--discovery https://discovery.etcd.io/bb0e48ca0da0ec3e5aa5f7275835c60c`

- 注意：

  每次需要新生成token，不然重复启动会报错

#### 配置并启动
- 创建配置文件
  * etcd.config
 
    `name:                        only-etcd`

    `data-dir:                    /data/etcd/only.etcd`

    `listen-client-urls:          http://0.0.0.0:2379`

    `advertise-client-urls:       http://0.0.0.0:2379`

    `listen-peer-urls:            http://118.61.126.51:2380`

    `initial-advertise-peer-urls: http://118.61.126.51:2380`

    `initial-cluster:             only-etcd=http://118.61.126.51:2380`

    `initial-cluster-token:       only-etcd-token`

    `initial-cluster-state:       new`
    
- 启动

    `etcd --config-file=/usr/local/etcd/etcd.conf`
- 使用Python操作

  `import etcd3`
  
  `client = etcd3.client(host='118.61.126.51', port=2379)`
  
  `print('get test')`
  
  `client.put('/key', 'dooot')`
  
  `kv, kvMeta = client.get('/key')`
  
  `print('get value: %s' % kv)`
  
#### next

- 安装CoreOS，系统自带etcd。
- 查看版本：`etcd2 --version` 如果想要升级到3，可以[点击前往](https://coreos.com/etcd/docs/3.2.15/upgrades/upgrade_3_0.html#upgrade-procedure)
- CoreOS集群+etcd集群  未完待续



