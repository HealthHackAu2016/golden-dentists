-- MySQL dump 10.15  Distrib 10.0.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dentists
-- ------------------------------------------------------
-- Server version	10.0.27-MariaDB-0ubuntu0.16.04.1

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
-- Table structure for table `dentists`
--

DROP TABLE IF EXISTS `dentists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dentists` (
  `name` varchar(20) NOT NULL DEFAULT '',
  `street` varchar(40) DEFAULT NULL,
  `suburb` varchar(20) DEFAULT NULL,
  `postcode` varchar(4) DEFAULT NULL,
  `abn` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dentists`
--

LOCK TABLES `dentists` WRITE;
/*!40000 ALTER TABLE `dentists` DISABLE KEYS */;
INSERT INTO `dentists` VALUES ('Dr Bertha','45 Johnny St','Spring Hill','4001','88066729648'),('Dr Jane','134 Rode Rd','Kedron','4008','80803099661'),('Dr Nick','12 Smith St','Chermside','4009','69049837072'),('Dr Tom','56 Ann St','Brisbane City','4000','52517659161');
/*!40000 ALTER TABLE `dentists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices` (
  `invoice_number` varchar(20) NOT NULL DEFAULT '',
  `price` varchar(6) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `dentist` varchar(20) DEFAULT NULL,
  `patient_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`invoice_number`),
  KEY `fk_code` (`code`),
  KEY `fk_dentist` (`dentist`),
  CONSTRAINT `fk_code` FOREIGN KEY (`code`) REFERENCES `items` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `fk_dentist` FOREIGN KEY (`dentist`) REFERENCES `dentists` (`name`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES ('001','245','D522','Dr Nick','Jane Doe'),('002','600','D522','Dr Nick','Sally Ree'),('003','450','D522','Dr Nick','Bobby Ray'),('004','678','D522','Dr Jane','Barry Fly'),('005','135','D522','Dr Jane','Jane Doe'),('006','478','D522','Dr Jane','Sally Ree'),('007','799','D522','Dr Tom','Gary Go'),('008','1002','D522','Dr Tom','Jane Doe'),('009','590','D522','Dr Tom','Sally Ree'),('010','132','D522','Dr Bertha','Mary By'),('011','180','D522','Dr Bertha','Jane Doe'),('012','115','D522','Dr Bertha','Sally Ree'),('013','3000','D618','Dr Nick','Jane Doe'),('014','2800','D618','Dr Nick','Sally Ree'),('015','3100','D618','Dr Nick','Bobby Ray'),('016','1000','D618','Dr Jane','Barry Fly'),('017','990','D618','Dr Jane','Sally Ree'),('018','789','D618','Dr Jane','Bobby Ray'),('019','879','D618','Dr Tom','Gary Go'),('020','999','D618','Dr Tom','Sally Ree'),('021','887','D618','Dr Tom','Bobby Ray'),('022','2560','D618','Dr Bertha','Mary By'),('023','2220','D618','Dr Bertha','Sally Ree'),('024','2130','D618','Dr Bertha','Bobby Ray'),('025','56','D011','Dr Nick','Jane Doe'),('026','259','D011','Dr Jane','Barry Fly'),('027','35','D011','Dr Tom','Gary Go'),('028','135','D011','Dr Bertha','Mary By');
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `code` varchar(10) NOT NULL DEFAULT '',
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES ('D011','Comprehensive oral examination'),('D522','Adhesive restoration - two surfaces  - anterior tooth'),('D618','Full crown - metallic  - indirect');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-16  8:21:12
