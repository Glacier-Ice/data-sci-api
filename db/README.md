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

