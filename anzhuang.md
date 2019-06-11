# 1.安装服务器端

## 1.1环境准备

<http://book.open-falcon.org/zh_0_2/quick_install/prepare.html>

0.2.1版本的openfalcon

<https://github.com/open-falcon/falcon-plus/releases/download/v0.2.1/open-falcon-v0.2.1.tar.gz>

###1.1.1安装redis

sudo apt-get install -y redis-sever

### 1.1.2安装mysql

sudo apt-get install -y mysql-server

Mysql数据库的密码记得更改为自己的

### 1.1.3初始化mysql的表结构

cd /tmp/ && git clone https://github.com/open-falcon/falcon-plus.git 

(若报错缺少git，请安装git，若报错将https换成git即可）

cd /tmp/falcon-plus/scripts/mysql/db_schema/

mysql -h 127.0.0.1 -u root -p < 1_uic-db-schema.sql

mysql -h 127.0.0.1 -u root -p < 2_portal-db-schema.sql

mysql -h 127.0.0.1 -u root -p < 3_dashboard-db-schema.sql

mysql -h 127.0.0.1 -u root -p < 4_graph-db-schema.sql

mysql -h 127.0.0.1 -u root -p < 5_alarms-db-schema.sql

rm -rf /tmp/falcon-plus/

## 1.2前端部署

<http://book.open-falcon.org/zh_0_2/quick_install/frontend.html>

### 1.2.1创建工作目录

export HOME=/home/front

export WORKSPACE=$HOME/open-falcon

mkdir -p $WORKSPACE

cd $WORKSPACE

### 1.2.2克隆组件代码

cd $WORKSPACE

git clone https://github.com/open-falcon/dashboard.git

### 1.2.3安装依赖包

apt-get install -y python-virtualenv

apt-get install -y slapd ldap-utils

apt-get install -y libmysqld-dev

apt-get install -y build-essential

apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev

cd $WORKSPACE/dashboard/

sudo virtualenv ./env

 ./env/bin/pip install -r pip_requirements.txt -i https://pypi.douban.com/simple

### 1.2.4 初始化数据库

环境准备已经初始化好了

### 1.2.5修改配置

dashboard的配置文件为： 'rrd/config.py'，请根据实际情况修改

\## API_ADDR 表示后端api组件的地址

API_ADDR = "http://127.0.0.1:8080/api/v1" 

\## 根据实际情况，修改PORTAL_DB_*, 默认用户名为root，默认密码为""

\## 根据实际情况，修改ALARM_DB_*, 默认用户名为root，默认密码为""

### 1.2.6 开发者**&生产环境**

./env/bin/python wsgi.py

 

bash control start

 

open http://127.0.0.1:8081 in your browser.

### 1.2.7查看日志

bash control tail

## 1.3服务器后端部署

<http://book.open-falcon.org/zh_0_2/quick_install/backend.html>

### 1.3.1环境部署

因为前端部署已经部署过了，因此可忽略

### 1.3.2创建工作目录

export FALCON_HOME=/home/work

export WORKSPACE=$FALCON_HOME/open-falcon

mkdir -p $WORKSPACE

###1.3.3 **解压缩二进制包**

**文件下载地址未提供，git上可提供压缩包**

**https://github.com/open-falcon/falcon-plus/releases**

0.2.1版本的openfalcon

<https://github.com/open-falcon/falcon-plus/releases/download/v0.2.1/open-falcon-v0.2.1.tar.gz>

tar -xzvf open-falcon-v0.2.1.tar.gz -C $WORKSPACE

### 1.3.4**确认配置文件数据库账号密码与实际是否相同**

cd $WORKSPACE

grep -Ilr 3306  ./ | xargs -n1 -- sed -i 's/root:/数据库用户名:数据库密码/g'

### 1.3.5启动后端

cd $WORKSPACE

./open-falcon start

 # 检查所有模块的启动状况

./open-falcon check

# 2.client端部署

## 2.1系统安装

### 2.1.1下载镜像

在树莓派官网下载官方镜像，可以直接下载带桌面版的镜像，本文使用的是桌面版的镜像。

PS：镜像可以在百度云分享链接内找到

树莓派官方地址 <https://www.raspberrypi.org/downloads/>

### 2.1.2**使用win10自带的磁盘管理工具，格式化SD卡**

![1557910293212](C:\Users\ldm\AppData\Local\Temp\1557910293212.png)

### 2.1.3**使用win32diskimager-1.0.0-install.exe，刷写镜像**

安装此软件，找到镜像，找到SD卡的盘符，进行刷写

PS：工具可以在百度云分享链接内找到

![1560240155343](C:\Users\ldm\AppData\Local\Temp\1560240155343.png)

### 3.1.4进入到系统

把sd卡插入到raspberry中，并且插入网线，鼠标，键盘，显示器等

开启ssh的连接，命令如下

\# service ssh start/restart

密码raspberry

1. 使用远程连接工具连接到raspberry，便可以操作

 

2. 使用apt-get update，更新raspberry的package list，下面是我常用软件list，可以直接复制安装

apt install -y vim

## 2.2安装**open-falcon的agent**

### 2.2.1安装go环境的步骤

#### 2.2.1.1下载go的包

这个Step1.下载go的包（我把包放在云服务器202.120.83.82上）

scp pi@<服务器ip>:/sourcecode/go1.10.1.linux-armv6l.tar.gz ./

#### 2.2.1.2解压go

tar xvf go1.10.1.linux-armv6l.tar.gz -C /usr/local

#### 2.2.1.3配置go的黄静变量到.bashrc

vim .bashrc

\#添加下面三行到最后

export GOPATH=/usr/local/go

export GOROOT=/usr/local/go

export PATH=$PATH:/usr/local/go/bin

\#退出编辑

source .bashrc

### 2.2.2**检查git和go环境**

apt install -y git

版本要求：git >= 1.7.5，go >= 1.6

检查版本命令：git version，go version

## 2.3下载open-falcon的agent部分

3.3.1创建文件夹，并clone仓库文件

mkdir -p $GOPATH/src/github.com/open-falcon

cd $GOPATH/src/github.com/open-falcon

git clone <https://github.com/open-falcon/falcon-plus.git>

chmod -R 777 falcon-plus/

cd /usr/local/go/src/github.com/open-falcon/falcon-plus/modules/agent/

3.3.2创建并修改cfg.json文件

cp cfg.example.json cfg.json

修改cfg.json文件 添加hostname=”自己起个名字” 和 ip=<服务器ip>

记得更改所有的ip，heartbeats和transfer的ip都更改为服务器的ip

go get

\# warning: GOPATH set to GOROOT (/usr/local/go) has no effect 

\# 这条警告可以忽略

./control build

./control start

\# 查看是否有开启的端口1988

netstat -tnlp

## 2.4**DHT11模块**

### 2.4.1下载安装DHT11的轮子

git clone https://github.com/adafruit/Adafruit_Python_DHT

 

cd Adafruit_Python_DHT/ 

python setup.py install

### 2.4.2在plugin中的script使用这个库

**demo**（这只是个使用案例与安装教程无关）

\#!/usr/bin/python

import Adafruit_DHT 

if __name__ == '__main__': 

​    sensor = Adafruit_DHT.DHT11 

​    humidity, temperature = Adafruit_DHT.read_retry(sensor, 04) 

​    print humidity

​    print temperature

## 2.5**plugin部分**

### 2.5.1修改cfg.json文件

"plugin": {

​        "enabled": true,

​        "dir": "./plugin",

​        "git": "https://github.com/colabearwd/plugin.git",

​        #需要修改此处的git仓库地址

​        "logs": "./logs"

​    },

### 2.5.2激活plugin，拉取git中的代码

使用浏览器访问，http://<节点的ip>:1988/plugin/update

看到返回success，即拉取成功

可以在下面文件夹内查看plugin

cd /usr/local/go/src/github.com/open-falcon/falcon-plus/modules/agent/plugin

cp config.py.default config.py
修改config.py文件

可以使用 auto.sh 来修改plugin里面文件的ip地址配置和权限设置

bash auto.sh 

（如果无法访问可采用curl http://<节点的ip>:1988/plugin/update方法，在服务器端的/home/work/open-falcon/也需要curl http://<服务器的ip>:1988/plugin/update其余步骤相同）

### 2.5.3在dashboard设置plugin的运行的节点 

![1557910360303](C:\Users\ldm\AppData\Local\Temp\1560240177104.png)

step1：创建hostgroup

![1557910375416](C:\Users\ldm\AppData\Local\Temp\1560240197845.png)

step2：添加host和添加plugin

![1557910387546](C:\Users\ldm\AppData\Local\Temp\1560240214506.png)

添加这个hostgroup的host

![1557910401554](C:\Users\ldm\AppData\Local\Temp\1560240229653.png)

添加这个hostgroup的需要执行的plugin的文件夹





# 3.部署api

# 3.1服务器端部署api

cd /home/

git clone https://github.com/colabearwd/api.git

cd api

切换分支git checkout dev01（查看分之git branch -a）

cd  /app/templates

vim openfalcon.html (根据实际的openfalcon地址修改)

对api/app/grpc_push文件夹进行更新

cd app

git clone https://github.com/colabearwd/xsentialgrpc.git

mv xsentialgrpc/ grpc_push

cd grpc_push

git checkout dev_grpc

更改配置

cd /home/api

cp config.py.default config.py

vim config.py(port按照自己要求填写，key、secret_key任意值但必须有，SQLALCHEMY_DATABASE_URI、name、password、api_addr、api_ip按照实际安装过程填写，)

把数据库的表导入数据库
mysql> create database myproject;
mysql -u 账号 -p 密码 myproject < myproject.sql

（根据实际open-falcon地址修改

vim  /home/api/app/templates/openfalcon.html的src地址内容）

虚拟化：virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

pip list(查看安装的 包)

screen -S run

source venv/bin/activate

python  run.py

screen -S sever

source venv/bin/activate

cd app/grpc_push

cp config.py.default config.py

vim config.py(ip服务器地址，port58081)

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./push.proto

（建立screen)

python my_server.py(建议如果下次在进入建议服务器与客户端都处于虚拟环境，避免环境不一样存在的问题)

## 3.2客户端部署api

cd /home/

git clone https://github.com/colabearwd/xsentialgrpc.git

cd xsentialgrpc

git checkout dev_grpc

cp config.py.default config.py

vim config.py(ip服务器地址，port58081)

apt-get install python3-venv
python3 -m venv venv

source venv/bin/activate

pip install -r requirement.txt

pip list(查看安装的 包)

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./push.proto

（建立screen)

screen -S curl

source venv/bin/activate

python consumer_curl_final.py

(按ctrl-a-d返回)

screen -S ping

source venv/bin/activate

python consumer_ping_final.py