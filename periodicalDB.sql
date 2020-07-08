-- MySQL dump 10.16  Distrib 10.1.44-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: periodicalDB
-- ------------------------------------------------------
-- Server version	10.1.44-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator_table`
--

DROP TABLE IF EXISTS `administrator_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrator_table` (
  `Admin_zh` char(9) COLLATE utf8_general_mysql500_ci NOT NULL,
  `Admin_password` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`Admin_zh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_table`
--

LOCK TABLES `administrator_table` WRITE;
/*!40000 ALTER TABLE `administrator_table` DISABLE KEYS */;
INSERT INTO `administrator_table` VALUES ('admin','admin'),('admin1','123456'),('admin2','123456');
/*!40000 ALTER TABLE `administrator_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow_table`
--

DROP TABLE IF EXISTS `borrow_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `borrow_table` (
  `B_id` int(11) NOT NULL AUTO_INCREMENT,
  `B_gh` varchar(50) COLLATE utf8_general_mysql500_ci NOT NULL,
  `B_name` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `B_qkmc` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `B_year` int(11) DEFAULT NULL,
  `B_volume` int(11) DEFAULT NULL,
  `B_issue` int(11) DEFAULT NULL,
  `B_jyrq` char(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `B_ghrq` char(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `B_ydyh` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`B_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_table`
--

LOCK TABLES `borrow_table` WRITE;
/*!40000 ALTER TABLE `borrow_table` DISABLE KEYS */;
INSERT INTO `borrow_table` VALUES (1,'E11714001','章三','自动化学报',2017,43,1,'2017.04.01','2020.06.15',NULL),(2,'E11714002','里四','计算机学报',2015,38,8,'2017.04.10',NULL,NULL),(3,'E11714003','汪五','统计研究',2014,31,1,'2017.04.22',NULL,NULL),(12,'E11714001',NULL,'计算机学报',2017,40,2,'2020.06.15','2020.06.15','E11714002'),(13,'E11714002',NULL,'计算机学报',2017,40,2,'2020.06.15',NULL,NULL),(14,'E11714000',NULL,'计算机学报',2017,40,1,'2020.06.15',NULL,NULL);
/*!40000 ALTER TABLE `borrow_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_table`
--

DROP TABLE IF EXISTS `catalog_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalog_table` (
  `Cg_qkmc` varchar(50) COLLATE utf8_general_mysql500_ci NOT NULL,
  `Cg_CN` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Cg_ISSN` varchar(9) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Cg_yfdm` varchar(6) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Cg_cbzq` varchar(3) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Cg_cbd` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Cg_zbdw` varchar(20) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`Cg_qkmc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_table`
--

LOCK TABLES `catalog_table` WRITE;
/*!40000 ALTER TABLE `catalog_table` DISABLE KEYS */;
INSERT INTO `catalog_table` VALUES ('统计研究','11-1302/C','1002-4565','82-14','月刊','北京','中国统计学会'),('自动化学报','11-1826/TP','0254-4156','2-180','月刊','北京','中国自动化学会'),('计算机学报','11-1826/TP','0254-4164','2-833','月刊','北京','中国科学院计算技术研究所'),('青年文摘','11-1222/C','1003-0565','2-031','半月刊','北京','中国青年出版社');
/*!40000 ALTER TABLE `catalog_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content_table`
--

DROP TABLE IF EXISTS `content_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content_table` (
  `Ct_ID` int(10) NOT NULL AUTO_INCREMENT,
  `Ct_qkmc` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_year` int(11) DEFAULT NULL,
  `Ct_volume` int(11) DEFAULT NULL,
  `Ct_issue` int(11) DEFAULT NULL,
  `Ct_title` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_author` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_page` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_keyword1` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_keyword2` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_keyword3` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_keyword4` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `Ct_keyword5` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`Ct_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content_table`
--

LOCK TABLES `content_table` WRITE;
/*!40000 ALTER TABLE `content_table` DISABLE KEYS */;
INSERT INTO `content_table` VALUES (1,'自动化学报',2017,43,1,'平行学习—机器学习的一个新型理 论框架','李力、林懿伦、曹东璞、郑南宁、王飞跃','1~8','机器学习','人工智能','平行学习','平行智能','平行系统及 理论'),(2,'自动化学报',2017,43,1,'基于庞特里亚金极小值原理的多运 载体有限时间编队控制','耿志勇','40~59','有限时间编 队控制','一致性','多运载体','极小值原理',NULL),(3,'自动化学报',2017,43,1,'基于计算实验的公共交通需求预测 方法','陈曦、彭蕾、李炜','60~71','计算实验','交通需求预测','Agent',NULL,'BDI模型'),(4,'统计研究',2014,31,1,'大数据时代对统计学的挑战','邱东','16~22','大数据','信息','噪声','数据科学','统计学'),(5,'计算机学报',2015,38,8,'基于粒计算的大数据处理','徐计、王国胤、于洪','1497~1517','粒计算','大数据','云计算','深度学习',NULL),(16,'意林',2020,23,3,'时间管理','向螺','22-28','时间管理','高效工作','精力旺盛','人际关系','None');
/*!40000 ALTER TABLE `content_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_table`
--

DROP TABLE IF EXISTS `register_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `register_table` (
  `R_ID` int(11) NOT NULL AUTO_INCREMENT,
  `R_qkmc` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `R_year` int(11) DEFAULT NULL,
  `R_volume` int(11) DEFAULT NULL,
  `R_issue` int(11) DEFAULT NULL,
  PRIMARY KEY (`R_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_table`
--

LOCK TABLES `register_table` WRITE;
/*!40000 ALTER TABLE `register_table` DISABLE KEYS */;
INSERT INTO `register_table` VALUES (1,'计算机学报',2015,38,8),(2,'统计研究',2014,31,1),(3,'计算机学报',2017,40,2),(4,'计算机学报',2017,40,1),(5,'自动化学报',2017,43,3),(6,'自动化学报',2017,43,2),(7,'自动化学报',2017,43,1),(8,'计算机学报',2015,35,8),(11,'计算机学报',2015,38,3);
/*!40000 ALTER TABLE `register_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_table`
--

DROP TABLE IF EXISTS `subscription_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_table` (
  `S_qkmc` varchar(50) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `S_yfdm` varchar(11) COLLATE utf8_general_mysql500_ci NOT NULL,
  `S_zdnf` int(11) NOT NULL,
  PRIMARY KEY (`S_yfdm`,`S_zdnf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_table`
--

LOCK TABLES `subscription_table` WRITE;
/*!40000 ALTER TABLE `subscription_table` DISABLE KEYS */;
INSERT INTO `subscription_table` VALUES ('自动化学报','2-180',2016),('自动化学报','2-180',2017),('自动化学报','2-180',2018),('计算机学报','2-833',2016),('计算机学报','2-833',2017),('计算机学报','2-833',2018),('计算机工程','4-310',2016),('读者','54-17',2020),('统计研究','82-14',2016),('统计研究','82-14',2017);
/*!40000 ALTER TABLE `subscription_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_table`
--

DROP TABLE IF EXISTS `user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_table` (
  `User_gh` char(9) COLLATE utf8_general_mysql500_ci NOT NULL,
  `User_name` varchar(10) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  `User_password` varchar(20) COLLATE utf8_general_mysql500_ci DEFAULT NULL,
  PRIMARY KEY (`User_gh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_table`
--

LOCK TABLES `user_table` WRITE;
/*!40000 ALTER TABLE `user_table` DISABLE KEYS */;
INSERT INTO `user_table` VALUES ('E11714000',NULL,'123'),('E11714001','章三','111111'),('E11714002','里四','222222'),('E11714003','汪五','333333');
/*!40000 ALTER TABLE `user_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-15 18:10:35
