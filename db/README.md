We recommend to use postgres docker to run the database server:
```
docker pull postgres:10
docker run -it --rm -v $PWD:/data -e POSTGRES_PASSWORD=abc -p 5432:5432 postgres:10
```
Then in another shell terminal, use `psql -h 127.0.0.1 -p 5432 -U postgres` to
connect to the server. Then
```
create database data;
\c data;
\i area_city.sql;
\i area_province.sql;
\i area_relation.sql;
```
Thus the database schema is successfully intialized.

epidemic是go写的存储疫情数据代码，后面考虑用python改一下。现使用了两张表，详细如下：

省级表：area_province

| 字段            | 类型    | 备注   |
| --------------- | ------- | ------ |
| id              | serial  | 主键   |
| curday          | date    | 日期   |
| province_name   | varchar | 省名   |
| province_code   | int     | 编号   |
| confirmed_count | bigint  | 确诊数 |
| cured_count     | bigint  | 治愈数 |
| dead_count      | bigint  | 死亡数 |
| suspected_count | bigint  | 疑似数 |



城市表：area_city

| 字段            | 类型    | 备注   |
| --------------- | ------- | ------ |
| id              | serial  | 主键   |
| curday          | date    | 日期   |
| city_name       | varchar | 城市名 |
| city_code       | int     | 编号   |
| confirmed_count | bigint  | 确诊数 |
| cured_count     | bigint  | 治愈数 |
| dead_count      | bigint  | 死亡数 |
| suspected_count | bigint  | 疑似数 |

