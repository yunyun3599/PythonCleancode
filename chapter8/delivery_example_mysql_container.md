## mock_patch_dellivery_example.py
상단 파일의 Delivery 객체에 대한 DB connection을 실제로 구축하는 방법

### 아래 container 구축
```shell
docker run --name mysql_tmp -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mysql:latest
```

### 데이터 insert
테스트를 위한 데이터를 INSERT
```shell
docker exec -ti mysql_tmp bash
mysql -u root -p    # pwd = 1234

create table delivery (
 Id int not null auto_increment,
 status varchar(20),
 update_time datetime default now() on update now(),
 primary key (id)
);

Insert into delivery (status) value("on_delivery")
```