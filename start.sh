
docker run -d --name mymariadb --env  MARIADB_ROOT_PASSWORD=123456 -p 3306:3306 --network some-network mariadb
docker exec  -it mymariadb bin/bash

sleep 10

mysql -uroot -p123456
create database dmeo;
show databases;
use dmeo;
sleep 5
create table user_info(id int(20) not null primary key,name varchar(50),age int(20),sex varchar(10),phone int(30));

insert into user_info values(1,'zhangsan',18,'nan',123456);
select * from user_info;

exit

exit
sleep 5

docker build --tag python_test .
docker run -d -p 5000:5000 --name py-test --link mymariadb --network some-network python_test
