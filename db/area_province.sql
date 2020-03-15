/*
Navicat PGSQL Data Transfer

Source Server         : wuhan
Source Server Version : 101000
Source Host           : 152.136.160.189:5432
Source Database       : wuhandb
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 101000
File Encoding         : 65001

Date: 2020-02-17 13:22:02
*/


-- ----------------------------
-- Table structure for area_province
-- ----------------------------
DROP TABLE IF EXISTS "public"."area_province";
CREATE TABLE "public"."area_province" (
"id" serial primary key,
"curday" date,
"province_name" varchar(255) COLLATE "default",
"province_code" int4,
"confirmed_count" int8,
"cured_count" int8,
"dead_count" int8,
"suspected_count" int8
)
WITH (OIDS=FALSE)

;

