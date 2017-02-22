/*
Navicat MySQL Data Transfer

Source Server         : kingja
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : qsbk

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2017-02-21 16:28:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for duanzi
-- ----------------------------
DROP TABLE IF EXISTS `duanzi`;
CREATE TABLE `duanzi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `icon` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of duanzi
-- ----------------------------
SET FOREIGN_KEY_CHECKS=1;
