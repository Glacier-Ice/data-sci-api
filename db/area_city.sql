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

Date: 2020-02-17 13:21:46
*/


-- ----------------------------
-- Table structure for area_city
-- ----------------------------
DROP TABLE IF EXISTS "public"."area_city";
CREATE TABLE "public"."area_city" (
"id" SERIAL PRIMARY KEY,
"curday" date,
"city_name" varchar(255) COLLATE "default",
"city_code" int4,
"confirmed_count" int8,
"cured_count" int8,
"dead_count" int8,
"suspected_count" int8
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By
-- ----------------------------
