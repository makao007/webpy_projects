create database smzdm;
drop table if exists item;
create table item (id int primary key auto_increment, title varchar(1024), 
    summary varchar(2048), link varchar(2048), image varchar(2048), link_md5 char(32), fetch_time datetime ) 
        DEFAULT CHARACTER SET utf8;
alter table item add unique (link_md5);


