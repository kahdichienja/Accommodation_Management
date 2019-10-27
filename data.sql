-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

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
-- Table structure for table `Profile_paymentrequestheaders`
--

DROP TABLE IF EXISTS `Profile_paymentrequestheaders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_paymentrequestheaders` (
  `id` varchar(0) DEFAULT NULL,
  `merchant_request_id` varchar(0) DEFAULT NULL,
  `checkout_request_id` varchar(0) DEFAULT NULL,
  `response_description` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL,
  `phone_number_used_for_payment` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_paymentrequestheaders`
--

LOCK TABLES `Profile_paymentrequestheaders` WRITE;
/*!40000 ALTER TABLE `Profile_paymentrequestheaders` DISABLE KEYS */;
/*!40000 ALTER TABLE `Profile_paymentrequestheaders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profile_roomateselection`
--

DROP TABLE IF EXISTS `Profile_roomateselection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_roomateselection` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `user_roomate_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_roomateselection`
--

LOCK TABLES `Profile_roomateselection` WRITE;
/*!40000 ALTER TABLE `Profile_roomateselection` DISABLE KEYS */;
/*!40000 ALTER TABLE `Profile_roomateselection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profile_tenantprofile`
--

DROP TABLE IF EXISTS `Profile_tenantprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_tenantprofile` (
  `id` tinyint(4) DEFAULT NULL,
  `full_name` varchar(5) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `user_picture` varchar(51) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_tenantprofile`
--

LOCK TABLES `Profile_tenantprofile` WRITE;
/*!40000 ALTER TABLE `Profile_tenantprofile` DISABLE KEYS */;
INSERT INTO `Profile_tenantprofile` VALUES (1,'Ahoro',254712698982,'tenant_profile/app-apple-business-38295_Lj3mgbL.jpg','2019-10-11',1);
/*!40000 ALTER TABLE `Profile_tenantprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` tinyint(4) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `codename` varchar(28) DEFAULT NULL,
  `name` varchar(34) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_landlordprofile','Can add landlord profile'),(26,7,'change_landlordprofile','Can change landlord profile'),(27,7,'delete_landlordprofile','Can delete landlord profile'),(28,7,'view_landlordprofile','Can view landlord profile'),(29,8,'add_tenantprofile','Can add tenant profile'),(30,8,'change_tenantprofile','Can change tenant profile'),(31,8,'delete_tenantprofile','Can delete tenant profile'),(32,8,'view_tenantprofile','Can view tenant profile'),(33,9,'add_hostelcontact','Can add hostel contact'),(34,9,'change_hostelcontact','Can change hostel contact'),(35,9,'delete_hostelcontact','Can delete hostel contact'),(36,9,'view_hostelcontact','Can view hostel contact'),(37,10,'add_hostelhomepage','Can add hostel home page'),(38,10,'change_hostelhomepage','Can change hostel home page'),(39,10,'delete_hostelhomepage','Can delete hostel home page'),(40,10,'view_hostelhomepage','Can view hostel home page'),(41,11,'add_hostelgallary','Can add hostel gallary'),(42,11,'change_hostelgallary','Can change hostel gallary'),(43,11,'delete_hostelgallary','Can delete hostel gallary'),(44,11,'view_hostelgallary','Can view hostel gallary'),(45,12,'add_hostelservice','Can add hostel service'),(46,12,'change_hostelservice','Can change hostel service'),(47,12,'delete_hostelservice','Can delete hostel service'),(48,12,'view_hostelservice','Can view hostel service'),(49,13,'add_hostelplan','Can add hostel plan'),(50,13,'change_hostelplan','Can change hostel plan'),(51,13,'delete_hostelplan','Can delete hostel plan'),(52,13,'view_hostelplan','Can view hostel plan'),(53,14,'add_paymentrequestheaders','Can add payment request headers'),(54,14,'change_paymentrequestheaders','Can change payment request headers'),(55,14,'delete_paymentrequestheaders','Can delete payment request headers'),(56,14,'view_paymentrequestheaders','Can view payment request headers'),(57,15,'add_lnmonline','Can add lnm online'),(58,15,'change_lnmonline','Can change lnm online'),(59,15,'delete_lnmonline','Can delete lnm online'),(60,15,'view_lnmonline','Can view lnm online'),(61,16,'add_landlordprofile','Can add landlord profile'),(62,16,'change_landlordprofile','Can change landlord profile'),(63,16,'delete_landlordprofile','Can delete landlord profile'),(64,16,'view_landlordprofile','Can view landlord profile'),(65,17,'add_roomateselection','Can add roomate selection'),(66,17,'change_roomateselection','Can change roomate selection'),(67,17,'delete_roomateselection','Can delete roomate selection'),(68,17,'view_roomateselection','Can view roomate selection');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` tinyint(4) DEFAULT NULL,
  `password` varchar(78) DEFAULT NULL,
  `last_login` varchar(10) DEFAULT NULL,
  `is_superuser` tinyint(4) DEFAULT NULL,
  `username` varchar(11) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL,
  `email` varchar(11) DEFAULT NULL,
  `is_staff` tinyint(4) DEFAULT NULL,
  `is_active` tinyint(4) DEFAULT NULL,
  `date_joined` varchar(10) DEFAULT NULL,
  `last_name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$UA2jCJh386Bw$k8ufwfbDLeFjTFpw2NVl5nevWt8gbvTs5i5aDPh+lpA=','2019-10-09',1,'user','','',1,1,'2019-10-06',''),(2,'pbkdf2_sha256$150000$vLDykdlxkeLb$UuKl4mDY2lLXmKsur2s72cJdvv/o7w+jU6Prb4pSxD0=','',0,'infweinfiow','','user@g.org',0,1,'2019-10-08',''),(3,'pbkdf2_sha256$150000$nafqe3GffLoB$UKjK+h+cXV1BxxcqDb/0w5w6P+gidmy6MBYxbd5fpPU=','2019-10-09',1,'Toast','','user@g.org',1,1,'',''),(4,'pbkdf2_sha256$150000$bqXDhktRjaut$qw+jYC9mA7HLi5gqaCjwJYndWZMmRFGEHQ+nHq7kQUQ=','2019-10-09',0,'Toast2','','user3@g.org',0,1,'2019-10-08',''),(5,'pbkdf2_sha256$150000$E7bChZY1rBP5$55P3NiTCRH3hxxRVOrZ9wdHExrdmKgU1wdUCsyIaXzE=','',0,'Toast3','','user4@g.org',0,1,'2019-10-08','');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` tinyint(4) DEFAULT NULL,
  `action_time` varchar(10) DEFAULT NULL,
  `object_id` tinyint(4) DEFAULT NULL,
  `object_repr` varchar(20) DEFAULT NULL,
  `change_message` varchar(48) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `action_flag` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-10-06',1,'Vatican Cots Hostel','[{\"added\": {}}]',7,1,1),(2,'2019-10-07',1,'Vatican Cots Hostel','[{\"changed\": {\"fields\": [\"your_phone_number\"]}}]',7,1,2),(3,'2019-10-08',3,'Toast','[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1,2),(4,'2019-10-09',3,'Toast','[{\"changed\": {\"fields\": [\"is_superuser\"]}}]',4,1,2),(5,'2019-10-09',1,'Vatican Cots Hostel','',7,1,3),(6,'2019-10-09',2,'Vatican Cots Hostel','',16,1,3),(7,'2019-10-09',3,'Vatican Cotts Hostel','',16,1,3),(8,'2019-10-11',1,'Ahoro Profile','[{\"added\": {}}]',8,1,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` tinyint(4) DEFAULT NULL,
  `app_label` varchar(12) DEFAULT NULL,
  `model` varchar(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'Profile','landlordprofile'),(14,'Profile','paymentrequestheaders'),(17,'Profile','roomateselection'),(8,'Profile','tenantprofile'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'landloard','hostelcontact'),(11,'landloard','hostelgallary'),(10,'landloard','hostelhomepage'),(13,'landloard','hostelplan'),(12,'landloard','hostelservice'),(16,'landloard','landlordprofile'),(15,'mpesa','lnmonline'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` tinyint(4) DEFAULT NULL,
  `app` varchar(12) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `applied` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-10-06'),(2,'auth','0001_initial','2019-10-06'),(3,'admin','0001_initial','2019-10-06'),(4,'admin','0002_logentry_remove_auto_add','2019-10-06'),(5,'admin','0003_logentry_add_action_flag_choices','2019-10-06'),(6,'contenttypes','0002_remove_content_type_name','2019-10-06'),(7,'auth','0002_alter_permission_name_max_length','2019-10-06'),(8,'auth','0003_alter_user_email_max_length','2019-10-06'),(9,'auth','0004_alter_user_username_opts','2019-10-06'),(10,'auth','0005_alter_user_last_login_null','2019-10-06'),(11,'auth','0006_require_contenttypes_0002','2019-10-06'),(12,'auth','0007_alter_validators_add_error_messages','2019-10-06'),(13,'auth','0008_alter_user_username_max_length','2019-10-06'),(14,'auth','0009_alter_user_last_name_max_length','2019-10-06'),(15,'auth','0010_alter_group_name_max_length','2019-10-06'),(16,'auth','0011_update_proxy_permissions','2019-10-06'),(17,'sessions','0001_initial','2019-10-06'),(18,'Profile','0001_initial','2019-10-06'),(19,'Profile','0002_auto_20191006_2305','2019-10-06'),(20,'landloard','0001_initial','2019-10-06'),(21,'landloard','0002_hostelplan','2019-10-06'),(22,'Profile','0003_paymentrequestheaders','2019-10-07'),(23,'mpesa','0001_initial','2019-10-07'),(24,'mpesa','0002_auto_20190831_2141','2019-10-07'),(25,'mpesa','0003_auto_20190831_2214','2019-10-07'),(26,'mpesa','0004_auto_20190831_2217','2019-10-07'),(27,'Profile','0004_auto_20191007_0056','2019-10-07'),(28,'Profile','0005_auto_20191009_1233','2019-10-09'),(29,'Profile','0006_auto_20191009_1332','2019-10-09'),(30,'landloard','0003_auto_20191009_1415','2019-10-09'),(31,'Profile','0007_auto_20191009_1415','2019-10-09'),(32,'Profile','0008_auto_20191011_0125','2019-10-11');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(32) DEFAULT NULL,
  `session_data` varchar(252) DEFAULT NULL,
  `expire_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('yd94ey54hzjy0wu0ysh6tr3qs8o95xy9','NDNlYjIzM2ZiM2NhY2E2NzgzYTE3YTQ4ODE1NzY2YjczYzUyOTVlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDZkMzk4ODFmMDEwOTY3YzNhZjk4NGM1NTZhZDkxYzI2YzdhNjE2In0=','2019-10-22'),('95ddqfqt2uye6lszlbs1cfeaabbkaf2x','NDNlYjIzM2ZiM2NhY2E2NzgzYTE3YTQ4ODE1NzY2YjczYzUyOTVlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDZkMzk4ODFmMDEwOTY3YzNhZjk4NGM1NTZhZDkxYzI2YzdhNjE2In0=','2019-10-23'),('bhmo5zpsfa1mus7oioxdzes1yr2l7fah','NDNlYjIzM2ZiM2NhY2E2NzgzYTE3YTQ4ODE1NzY2YjczYzUyOTVlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDZkMzk4ODFmMDEwOTY3YzNhZjk4NGM1NTZhZDkxYzI2YzdhNjE2In0=','2019-10-23');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelcontact`
--

DROP TABLE IF EXISTS `landloard_hostelcontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelcontact` (
  `id` varchar(0) DEFAULT NULL,
  `hostel_phone_number` varchar(0) DEFAULT NULL,
  `hostel_mail` varchar(0) DEFAULT NULL,
  `payment_method` varchar(0) DEFAULT NULL,
  `hostel_address` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelcontact`
--

LOCK TABLES `landloard_hostelcontact` WRITE;
/*!40000 ALTER TABLE `landloard_hostelcontact` DISABLE KEYS */;
/*!40000 ALTER TABLE `landloard_hostelcontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelgallary`
--

DROP TABLE IF EXISTS `landloard_hostelgallary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelgallary` (
  `id` varchar(0) DEFAULT NULL,
  `photo_description` varchar(0) DEFAULT NULL,
  `photo` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelgallary`
--

LOCK TABLES `landloard_hostelgallary` WRITE;
/*!40000 ALTER TABLE `landloard_hostelgallary` DISABLE KEYS */;
/*!40000 ALTER TABLE `landloard_hostelgallary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelhomepage`
--

DROP TABLE IF EXISTS `landloard_hostelhomepage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelhomepage` (
  `id` varchar(0) DEFAULT NULL,
  `welcoming_message` varchar(0) DEFAULT NULL,
  `background_image` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelhomepage`
--

LOCK TABLES `landloard_hostelhomepage` WRITE;
/*!40000 ALTER TABLE `landloard_hostelhomepage` DISABLE KEYS */;
/*!40000 ALTER TABLE `landloard_hostelhomepage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelplan`
--

DROP TABLE IF EXISTS `landloard_hostelplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelplan` (
  `id` varchar(0) DEFAULT NULL,
  `single_room_desc` varchar(0) DEFAULT NULL,
  `double_room_desc` varchar(0) DEFAULT NULL,
  `self_contained` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelplan`
--

LOCK TABLES `landloard_hostelplan` WRITE;
/*!40000 ALTER TABLE `landloard_hostelplan` DISABLE KEYS */;
/*!40000 ALTER TABLE `landloard_hostelplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelservice`
--

DROP TABLE IF EXISTS `landloard_hostelservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelservice` (
  `id` varchar(0) DEFAULT NULL,
  `security` varchar(0) DEFAULT NULL,
  `water_supply` varchar(0) DEFAULT NULL,
  `power_supply` varchar(0) DEFAULT NULL,
  `bed_size` varchar(0) DEFAULT NULL,
  `room_size` varchar(0) DEFAULT NULL,
  `table_and_chair_availabitity` varchar(0) DEFAULT NULL,
  `hostel_name_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelservice`
--

LOCK TABLES `landloard_hostelservice` WRITE;
/*!40000 ALTER TABLE `landloard_hostelservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `landloard_hostelservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_landlordprofile`
--

DROP TABLE IF EXISTS `landloard_landlordprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_landlordprofile` (
  `id` tinyint(4) DEFAULT NULL,
  `hostel_name` varchar(13) DEFAULT NULL,
  `hostel_location` varchar(16) DEFAULT NULL,
  `your_full_name` varchar(14) DEFAULT NULL,
  `your_phone_number` bigint(20) DEFAULT NULL,
  `your_picture` varchar(33) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_landlordprofile`
--

LOCK TABLES `landloard_landlordprofile` WRITE;
/*!40000 ALTER TABLE `landloard_landlordprofile` DISABLE KEYS */;
INSERT INTO `landloard_landlordprofile` VALUES (1,'Vatican Cotts','Rongo University','Kah Di Chienja',798728372,'landlord/glider-toxic_Cpn5FrO.jpg','2019-10-09',3),(4,'Jersey','Rongo University','Kah Di Chienja',798728372,'landlord/glider-toxic_V790fu6.jpg','2019-10-09',1);
/*!40000 ALTER TABLE `landloard_landlordprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mpesa_lnmonline`
--

DROP TABLE IF EXISTS `mpesa_lnmonline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mpesa_lnmonline` (
  `id` varchar(0) DEFAULT NULL,
  `fail_merchant_request_id` varchar(0) DEFAULT NULL,
  `fail_result_code` varchar(0) DEFAULT NULL,
  `fail_result_description` varchar(0) DEFAULT NULL,
  `merchant_request_id` varchar(0) DEFAULT NULL,
  `result_code` varchar(0) DEFAULT NULL,
  `result_description` varchar(0) DEFAULT NULL,
  `saccess_amount` varchar(0) DEFAULT NULL,
  `saccess_balance` varchar(0) DEFAULT NULL,
  `saccess_mpesa_receipt_number` varchar(0) DEFAULT NULL,
  `saccess_phone_number` varchar(0) DEFAULT NULL,
  `saccess_transaction_date` varchar(0) DEFAULT NULL,
  `success_result_description` varchar(0) DEFAULT NULL,
  `checkout_request_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mpesa_lnmonline`
--

LOCK TABLES `mpesa_lnmonline` WRITE;
/*!40000 ALTER TABLE `mpesa_lnmonline` DISABLE KEYS */;
/*!40000 ALTER TABLE `mpesa_lnmonline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(29) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',32),('django_admin_log',8),('django_content_type',17),('auth_permission',68),('auth_user',5),('auth_group',0),('mpesa_lnmonline',0),('landloard_hostelcontact',0),('landloard_hostelgallary',0),('landloard_hostelhomepage',0),('landloard_hostelplan',0),('landloard_hostelservice',0),('landloard_landlordprofile',4),('Profile_tenantprofile',1),('Profile_paymentrequestheaders',0);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:30
