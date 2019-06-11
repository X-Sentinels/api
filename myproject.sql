-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: myproject
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `args_curl`
--

DROP TABLE IF EXISTS `args_curl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `args_curl` (
  `args_id` int(8) NOT NULL AUTO_INCREMENT,
  `args_ipversion` tinyint(1) DEFAULT NULL,
  `args_url` varchar(100) DEFAULT NULL,
  `args_timeout` int(11) DEFAULT NULL,
  PRIMARY KEY (`args_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `args_ping`
--

DROP TABLE IF EXISTS `args_ping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `args_ping` (
  `args_id` int(8) NOT NULL AUTO_INCREMENT,
  `args_ipversion` tinyint(1) DEFAULT NULL,
  `args_url` varchar(100) DEFAULT NULL,
  `args_packagesize` int(10) DEFAULT NULL,
  `args_count` int(10) DEFAULT NULL,
  `args_timeout` int(10) DEFAULT NULL,
  PRIMARY KEY (`args_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `curl_res`
--

DROP TABLE IF EXISTS `curl_res`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `curl_res` (
  `curl_endpoint` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `curl_ipversion` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `curl_targeturl` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `curl_timestamp` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `curl_value` float(255,0) DEFAULT NULL,
  `curl_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`curl_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1843440 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `map`
--

DROP TABLE IF EXISTS `map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `map` (
  `map_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `map_desc` varchar(255) DEFAULT NULL COMMENT '描述',
  `map_ofid` int(11) DEFAULT NULL COMMENT 'openfalcon里面endpoint的id',
  `map_ofname` varchar(255) DEFAULT NULL COMMENT 'openfalcon里面endpoint的name',
  PRIMARY KEY (`map_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ping_res`
--

DROP TABLE IF EXISTS `ping_res`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ping_res` (
  `ping_endpoint` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `ping_ipversion` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `ping_targeturl` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `ping_timestamp` varchar(255) CHARACTER SET ascii DEFAULT NULL,
  `ping_value` float(255,0) DEFAULT NULL,
  `ping_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ping_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3094015 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `temporary_curlres`
--

DROP TABLE IF EXISTS `temporary_curlres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `temporary_curlres` (
  `curl_serialnum` varchar(255) NOT NULL,
  `curl_httpcode` varchar(255) DEFAULT NULL,
  `curl_httpconnect` varchar(255) DEFAULT NULL,
  `curl_nameloopup` varchar(255) DEFAULT NULL,
  `curl_redirect` varchar(255) DEFAULT NULL,
  `curl_pretransfer` varchar(255) DEFAULT NULL,
  `curl_connect` varchar(255) DEFAULT NULL,
  `curl_starttransfer` varchar(255) DEFAULT NULL,
  `curl_speeddownload` varchar(255) DEFAULT NULL,
  `curl_total` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`curl_serialnum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `temporary_pingres`
--

DROP TABLE IF EXISTS `temporary_pingres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `temporary_pingres` (
  `ping_serialnum` varchar(255) NOT NULL,
  `ping_lossrate` varchar(255) NOT NULL,
  `ping_maxtime` varchar(255) NOT NULL,
  `ping_averagetime` varchar(255) NOT NULL,
  PRIMARY KEY (`ping_serialnum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(8) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(64) NOT NULL,
  `user_passwd` varchar(256) NOT NULL,
  `user_admin` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19 22:20:01
insert INTO `args_ping` VALUES(1,0,"www.baidu.com",64,5,5);

insert INTO `args_curl` VALUES(1,0,"www.baidu.com",5);

INSERT INTO `curl_res` VALUES ('ubuntu-pi-test','curl4','www.163.com','1556595660',15,1),('ubuntu-pi-test','curl4','www.baidu.com','1556595660',6,2),('ubuntu-pi-test','curl6','www.qq.com','1556595660',19,3),('ubuntu-pi-test','curl4','www.163.com','1556595720',13,4),('ubuntu-pi-test','curl4','www.baidu.com','1556595720',7,5),('ubuntu-pi-test','curl6','www.qq.com','1556595720',19,6);

INSERT INTO `ping_res` VALUES ('ubuntu-pi-test','ipv4','www.114.com','1556595660',28,1),('ubuntu-pi-test','ipv4','www.163.com','1556595660',17,2),('ubuntu-pi-test','ipv4','www.baidu.com','1556595660',27,3),('ubuntu-pi-test','ipv4','www.qq.com','1556595660',4,4),('ubuntu-pi-test','ipv6','www.qq.com','1556595660',92,5),('ubuntu-pi-test','ipv4','www.114.com','1556595720',28,6),('ubuntu-pi-test','ipv4','www.163.com','1556595720',17,7),('ubuntu-pi-test','ipv4','www.baidu.com','1556595720',27,8),('ubuntu-pi-test','ipv4','www.qq.com','1556595720',4,9),('ubuntu-pi-test','ipv6','www.qq.com','1556595720',92,10);
