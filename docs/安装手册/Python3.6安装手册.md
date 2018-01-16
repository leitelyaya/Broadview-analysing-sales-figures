#  Python3.6安装手册

[TOC]

## 1.  RedHat安装

### 1.1 准备编译环境

```bash
yum groupinstall 'Development Tools'
yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel
```

### 1.2 下载Python3.6 代码包

```bash
wget  https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
```


### 1.3  安装Python3.6

```
tar Jxvf  Python-3.5.0.tar.xz
cd Python-3.6.4
./configure --prefix=/usr/local/python3
make && make install
```



做软链接：

```bash
[root@iZ23m1dgviaZ bin]# ln -s /usr/local/python3/bin/python3.6 /usr/local/bin/python3
[root@iZ23m1dgviaZ bin]# python3 --version
Python 3.6.4
[root@iZ23m1dgviaZ bin]# ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3
[root@iZ23m1dgviaZ bin]# pip3 --version
pip 9.0.1 from /usr/local/python3/lib/python3.6/site-packages (python 3.6)
```

### 1.4 安装IPython
IPython是Python的交互式Shell，提供了代码自动补完，自动缩进，高亮显示，执行Shell命令等非常有用的特性。特别是它的代码补完功能，例如：在输入zlib.之后按下Tab键，IPython会列出zlib模块下所有的属性、方法和类。完全可以取代自带的bash。

#### 1.4.1 下载ipython源码

```bash
wget https://pypi.python.org/packages/fa/50/974211502bd72873728d44c3013fe79875c819c8fb69f778bcfd67bc7d38/ipython-6.2.1.tar.gz#md5=6873d91d340c6069a4f7c2d65258523b
```

#### 1.4.2 安装依赖包

```bash
pip3 install traitlets
pip3 install pygments
pip3 install pexpect
pip3 install pickleshare
pip3 install prompt_toolkit
pip3 install simplegeneric
```


#### 1.4.3 安装ipython

```bash
[root@iZ23m1dgviaZ src]# tar zxvf ipython-6.2.1.tar.gz
[root@iZ23m1dgviaZ src]# cd ipython-6.2.1
[root@iZ23m1dgviaZ python3]# python3 setup.py install
```
该操作将会在site-packages目录中安装ipyhon的库文件，并在scripts目录中创建一个ipython脚本


#### 1.4.5 配置远程notebook
- 安装依赖环境

```
yum install sqlite-devel
```

- 重新编译Python

```bash
./configure --enable-loadable-sqlite-extensions --prefix=/usr/local/python3
make && make install
```

- 安装jupyter

```bash
pip3 install jupyter
```

- 创建软链接

```bash
ln -s /usr/local/python3/bin/jupyter /usr/local/bin/jupyter
```

- 生成配置文件

```
[root@iZ23m1dgviaZ bin]# jupyter notebook --generate-config
Writing default config to: /root/.jupyter/jupyter_notebook_config.py
```

- 进入ipython 生成一个密文的密码：(此时输入的密码为：ab123)

```
In [1]: from notebook.auth import passwd

In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:b2fb89bc68c3:65bb47afb3f4e5fcaf2bf9154a54ca15081f1e1c'

```

- 修改默认配置文件，如下所示

```
c.NotebookApp.ip='*'
c.NotebookApp.password = u'sha:ce...刚才复制的那个密文'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888 #随便指定一个端口
```
