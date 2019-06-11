# Nginx安装与配置



#### 本系统是基于ubuntu16.04安装过程，可参考链接[**安装**](https://blog.csdn.net/joyzhi/article/details/82947710)

安装前准备工作

安装依赖包 zlib，openssl，pcre 安装命令如下：

```
sudo apt-get install zlib1g-dev

sudo apt-get install libpcre3 libpcre3-dev 

sudo apt-get install openssl libssl-dev
```

安装过程

1. 此次采用了源码包编译安装方式，优点是可以自定义安装指定模块以及最新版本，方式更灵活，下载命令 

   ```
   wget http://nginx.org/download/nginx-1.16.0.tar.gz
   ```

2. 解压文件，下载文件位置放在/home/ubuntu文件夹下，使用命令解压

   ```
   tar -zxvf nginx-1.16.0.tar.gz 
   ```

   切换到解压文件夹中

   ```
   cd nginx-1.16.0/ 
   ```

3. 需要运行./configure,其作用主要是检查当前环境是否满足安装条件，并对即将安装的软件进行配置，本项目需要支持ipv6，需要添加这个模块，还支持了gzip和ssl等模块，配置命令如下

   ```
   ./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module --with-ipv6
   ```

4. 安装软件使用命令

   ```
   make && make install
   ```

配置过程

1. 安装完成之后，使用如下命令查看安装目录,显示nginx安装在 /usr/local/nginx下

   ```
   whereis nginx
   ```

2. 进入/usr/local/nginx/conf文件下，打开nginx的配置文件nginx.conf，配置ipv6的80端口域名转发

   ```
     server {
   
           listen [::]:80  ipv6only=on;
           server_name  x-sentinels-6.ecnu.edu.cn;
   
           root /var/www/html;
           location ~ /.well-known/acme-challenge{
                           allow all;
                   }
   
          location / {
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_pass http://localhost:8081;
   
           }
   }
   ```

   配置ipv6的3456端口域名转发，并加入http_auth_basic_module模块配置，进行相应的登录认证配置，登录用户名和密码放置在文件 /home/ubuntu/htpasswd/htpasswd.user 中，使用htpasswd-utils工具创建用户，参考[htpasswd](https://blog.csdn.net/qq_42996081/article/details/82114639)

   ```
     server {
   
           listen [::]:3456  ipv6only=on;
           server_name  x-sentinels-6.ecnu.edu.cn;
           
           root /var/www/html;
           location ~ /.well-known/acme-challenge{
                           allow all;
                   }
   
          location / {
                    proxy_set_header Host $http_host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_pass http://localhost:3456;
                    auth_basic "Administrator’s Area";
                    auth_basic_user_file /home/ubuntu/htpasswd/htpasswd.user;
                    autoindex on;
           }
   ```

3. nginx的启动命令如下

   ```
   sudo /usr/local/nginx/sbin/nginx
   ```

   nginx检查配置文件是否正确命令如下，正确返回ok和success

   ```
   sudo /usr/local/nginx/sbin/nginx -t
   ```

   nginx重启命令

   ```
   sudo /usr/local/nginx/sbin/nginx -s reload
   ```

   nginx停止命令

   ```
   sudo /usr/local/nginx/sbin/nginx -s stop
   ```

   





























