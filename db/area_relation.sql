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

Date: 2020-02-17 13:22:11
*/


-- ----------------------------
-- Table structure for area_relation
-- ----------------------------
DROP TABLE IF EXISTS "public"."area_relation";
CREATE TABLE "public"."area_relation" (
"area_type" varchar(255) COLLATE "default",
"area_name" varchar(255) COLLATE "default",
"code" int4
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Records of area_relation
-- ----------------------------

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------
