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
contaienr_name="velcom-nginx"
docker build -t velcom .
docker container stop ${contaienr_name}
docker container rm ${contaienr_name}
sleep 1
docker run --name ${contaienr_name} -d -p 18080:80 velcom
 ```
 
<p>&emsp;&emsp;因为flask连接数据库用的是flask内置的连接数据库的框架，在flask容器里具体连接MariaDB容器指令如下：</p>

 ```
 mysql -u root -h "127.0.0.1" -P 3306 -p${db_rootpass} -e "
 ```
 

<p>&emsp;&emsp;在flask运行之前，提前创建好数据库QA，指令如下：</p>

 ```
 contaienr_name="velcom-database"
db_username="velcom"
db_userpass="velcom_alksdjflkakjei"
db_rootpass="velcom_rootlkdjalienfklae"
db_name="velcom"
table_msg_name="velcom_msg"
docker run \
    --detach \
    --name ${contaienr_name} \
    --env MARIADB_USER=${db_username} \
    --env MARIADB_PASSWORD=${db_userpass} \
    --env MARIADB_ROOT_PASSWORD=${db_rootpass} \
    -p 3306:3306 \
    --network velcom_net \
    mariadb:latest
sudo apt install -y mysql-client
mysql -u root -h "127.0.0.1" -P 3306 -p${db_rootpass} -e "
CREATE DATABASE ${db_name};
 USE ${db_name};
 CREATE TABLE IF NOT EXISTS ${table_msg_name}
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
 
### <li>数据库中留言信息截图
 
<center>
  <img src="screenShot_img\5.png" width="400" height=""> 
  </center>

## 小组项目心得体会
 
<p>&emsp;&emsp;本项目论述了一个基于云南大学校园的网上留言板管理系统，重点讨论了开发系统的工具，开发环境的配置，后台数据库连接等技术。本系统只实现了留言板最基本的功能，该留言板管理系统简洁实用，而且界面友好，为教师和学生的交流提供了一个广阔的空间和平台。还有很多具体的功能还未实现，如置顶功能，留言板回复讨论功能等。</p>
