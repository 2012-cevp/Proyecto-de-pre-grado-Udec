CREATE DATABASE  IF NOT EXISTS `moneda` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `moneda`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: moneda
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `euro`
--

DROP TABLE IF EXISTS `euro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `euro` (
  `ideuro` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Precio` float NOT NULL,
  `Prediccion` double NOT NULL,
  PRIMARY KEY (`ideuro`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `euro`
--

LOCK TABLES `euro` WRITE;
/*!40000 ALTER TABLE `euro` DISABLE KEYS */;
INSERT INTO `euro` VALUES (1,'2022-04-15',4028.5,4068.71),(2,'2022-04-16',4027.5,4067.71),(3,'2022-04-17',4027.5,4067.71),(4,'2022-04-17',4027.5,4067.71),(5,'2022-04-17',4025.5,4065.71),(6,'2022-04-17',4025.5,4065.71),(7,'2022-04-17',4026,4066.21),(8,'2022-04-17',4026,4066.21),(9,'2022-04-17',4026,4066.21),(10,'2022-04-17',4026,4066.21),(11,'2022-04-17',4026,4066.21),(12,'2022-04-17',4023.5,4063.71),(13,'2022-04-17',4023,4063.21),(14,'2022-04-17',4023,4063.21),(15,'2022-04-18',4021,4061.21),(16,'2022-04-18',4021,4061.21),(17,'2022-04-18',4021,4061.21),(18,'2022-04-18',4021,4061.21),(19,'2022-04-18',4021,4061.21),(20,'2022-04-18',4021,4061.21),(21,'2022-04-18',4021,4061.21),(22,'2022-04-18',4021,4061.21),(23,'2022-04-18',4021,4061.21),(24,'2022-04-18',4021,4061.21),(25,'2022-04-18',4022,4062.21),(26,'2022-04-18',4021,4061.21),(27,'2022-04-18',4021,4061.21),(28,'2022-04-18',4021,4061.21),(29,'2022-04-18',4021,4061.21),(30,'2022-04-18',4024,4064.21),(31,'2022-04-18',4024,4064.21),(32,'2022-04-18',4024.5,4064.71),(33,'2022-04-18',4024.5,4064.71),(34,'2022-04-18',4023.5,5000),(35,'2022-04-18',4023.5,4063.71),(36,'2022-04-18',4017,4057.21),(37,'2022-04-18',4020,4060.21),(38,'2022-04-18',4020,4060.21),(39,'2022-04-23',4162,4202.21),(40,'2022-04-23',4162,4202.21),(41,'2022-04-23',4162,4202.21),(42,'2022-04-23',4162,4202.21),(43,'2022-04-23',4162,4202.21),(44,'2022-04-23',4162,4202.21),(45,'2022-04-23',4162,4202.21),(46,'2022-04-23',4162,4202.21);
/*!40000 ALTER TABLE `euro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27 14:10:16
