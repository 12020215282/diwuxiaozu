# diwuxiaozu
以docker容器的方式部署具有Web前端，具有业务层和数据库的应用程序。
## 项目功能简介

<p>&emsp;&emsp;本项目以docker容器的方式部署web应用。简单的实现了Python容器和mariadb容器，以及两个容器的通信，并以简单的web页面来进行验证。</p>

## 程序运行方式

### <li><b>大致流程</b>
<p>&emsp;&emsp;构建并运行mariadb容器，并且宿主机能够配置和访问数据库；宿主机再次运行包含flask的Python容器；完成两个容器之间的通信。</p>
 
### <li><b>具体流程</b>
<p>&emsp;&emsp;1、构建并运行mariadb容器，指令如下：</p>

 ```
docker search mariadb
docker pull mariadb
docker network rm velcom_net
docker network create some-network
docker run \ 
    -d \
    --name mymariadb \
    --env  MARIADB_ROOT_PASSWORD=123456 \
    -p 3306:3306 \
    --network some-network \
    mariadb
docker exec  -it mymariadb bin/bash
mysql -uroot -p123456
create database dmeo;
show databases;
use dmeo;
create table user_info(id int(20) not null primary key,
  -> name varchar(50),
  -> age int(20),
  -> sex varchar(10),
  -> phone varchar(30));
insert into user_info values(1,'zhangsan',18,'nan','123456789');
select * from user_info;
exit
exit 
 ```

<p>&emsp;&emsp;2、构建并运行Python容器，并实现与mariadb容器的通信，具体指令如下：</p>

 ```
Dockerfile内容如下：
# syntax=docker/dockerfile:1

FROM python:3.7
WORKDIR alpine/
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","app.py"]
 
构建Python容器并通信指令如下：
docker build -t python_test .
docker run \
  -d \
  -p 5000:5000 \
  --name py-test \
  --link mymariadb \
  --network some-network \
  python_test
 ```

<p>&emsp;&emsp;当以上步骤都完成之后，就可以运行flask的web应用了。</p>


## 项目截图
 
### <li>程序运行截图
 
<center>
  <img src="screenShot_img\1.png" width="400" height=""> 
  </center>
<center>
  <img src="screenShot_img\2.png" width="400" height=""> 
  </center>

<center>
  <img src="screenShot_img\3.png" width="400" height=""> 
  </center>

<center>
  <img src="screenShot_img\4.png" width="400" height=""> 
  </center>
