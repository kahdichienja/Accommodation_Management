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
-- Table structure for table `Profile_hostelpaymentplan`
--

DROP TABLE IF EXISTS `Profile_hostelpaymentplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_hostelpaymentplan` (
  `id` tinyint(4) DEFAULT NULL,
  `paymentplan_id` tinyint(4) DEFAULT NULL,
  `tenant_id` tinyint(4) DEFAULT NULL,
  `amountpaid` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_hostelpaymentplan`
--

LOCK TABLES `Profile_hostelpaymentplan` WRITE;
/*!40000 ALTER TABLE `Profile_hostelpaymentplan` DISABLE KEYS */;
INSERT INTO `Profile_hostelpaymentplan` VALUES (1,1,3,'6 000');
/*!40000 ALTER TABLE `Profile_hostelpaymentplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profile_paymentrequestheaders`
--

DROP TABLE IF EXISTS `Profile_paymentrequestheaders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_paymentrequestheaders` (
  `id` tinyint(4) DEFAULT NULL,
  `merchant_request_id` varchar(15) DEFAULT NULL,
  `checkout_request_id` varchar(38) DEFAULT NULL,
  `response_description` varchar(40) DEFAULT NULL,
  `phone_number_used_for_payment` bigint(20) DEFAULT NULL,
  `hostel_name_id` tinyint(4) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_paymentrequestheaders`
--

LOCK TABLES `Profile_paymentrequestheaders` WRITE;
/*!40000 ALTER TABLE `Profile_paymentrequestheaders` DISABLE KEYS */;
INSERT INTO `Profile_paymentrequestheaders` VALUES (1,'21546-1245644-1','ws_CO_DMZ_412503269_11112019073953344','Success. Request accepted for processing',254797324006,1,3,'2019-11-11'),(2,'21540-1246143-1','ws_CO_DMZ_2448736369_11112019074037658','Success. Request accepted for processing',254797324006,1,3,'2019-11-11');
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
  `is_accepted` varchar(0) DEFAULT NULL,
  `user_roomate` varchar(0) DEFAULT NULL
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
  `your_full_name` varchar(8) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `user_picture` varchar(25) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_tenantprofile`
--

LOCK TABLES `Profile_tenantprofile` WRITE;
/*!40000 ALTER TABLE `Profile_tenantprofile` DISABLE KEYS */;
INSERT INTO `Profile_tenantprofile` VALUES (1,'John Doe',254797324006,'tenant_profile/event3.jpg','2019-11-11',3);
/*!40000 ALTER TABLE `Profile_tenantprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profile_userhostelplan`
--

DROP TABLE IF EXISTS `Profile_userhostelplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile_userhostelplan` (
  `id` tinyint(4) DEFAULT NULL,
  `tenant_id` tinyint(4) DEFAULT NULL,
  `plan_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile_userhostelplan`
--

LOCK TABLES `Profile_userhostelplan` WRITE;
/*!40000 ALTER TABLE `Profile_userhostelplan` DISABLE KEYS */;
INSERT INTO `Profile_userhostelplan` VALUES (1,3,1);
/*!40000 ALTER TABLE `Profile_userhostelplan` ENABLE KEYS */;
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
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_tenantprofile','Can add tenant profile'),(26,7,'change_tenantprofile','Can change tenant profile'),(27,7,'delete_tenantprofile','Can delete tenant profile'),(28,7,'view_tenantprofile','Can view tenant profile'),(29,8,'add_roomateselection','Can add roomate selection'),(30,8,'change_roomateselection','Can change roomate selection'),(31,8,'delete_roomateselection','Can delete roomate selection'),(32,8,'view_roomateselection','Can view roomate selection'),(33,9,'add_paymentrequestheaders','Can add payment request headers'),(34,9,'change_paymentrequestheaders','Can change payment request headers'),(35,9,'delete_paymentrequestheaders','Can delete payment request headers'),(36,9,'view_paymentrequestheaders','Can view payment request headers'),(37,10,'add_userhostelplan','Can add user hostel plan'),(38,10,'change_userhostelplan','Can change user hostel plan'),(39,10,'delete_userhostelplan','Can delete user hostel plan'),(40,10,'view_userhostelplan','Can view user hostel plan'),(41,11,'add_hostelpaymentplan','Can add hostel paymentplan'),(42,11,'change_hostelpaymentplan','Can change hostel paymentplan'),(43,11,'delete_hostelpaymentplan','Can delete hostel paymentplan'),(44,11,'view_hostelpaymentplan','Can view hostel paymentplan'),(45,12,'add_landlordprofile','Can add landlord profile'),(46,12,'change_landlordprofile','Can change landlord profile'),(47,12,'delete_landlordprofile','Can delete landlord profile'),(48,12,'view_landlordprofile','Can view landlord profile'),(49,13,'add_hostelservice','Can add hostel service'),(50,13,'change_hostelservice','Can change hostel service'),(51,13,'delete_hostelservice','Can delete hostel service'),(52,13,'view_hostelservice','Can view hostel service'),(53,14,'add_hostelplan','Can add hostel plan'),(54,14,'change_hostelplan','Can change hostel plan'),(55,14,'delete_hostelplan','Can delete hostel plan'),(56,14,'view_hostelplan','Can view hostel plan'),(57,15,'add_hostelhomepage','Can add hostel home page'),(58,15,'change_hostelhomepage','Can change hostel home page'),(59,15,'delete_hostelhomepage','Can delete hostel home page'),(60,15,'view_hostelhomepage','Can view hostel home page'),(61,16,'add_hostelgallary','Can add hostel gallary'),(62,16,'change_hostelgallary','Can change hostel gallary'),(63,16,'delete_hostelgallary','Can delete hostel gallary'),(64,16,'view_hostelgallary','Can view hostel gallary'),(65,17,'add_hostelcontact','Can add hostel contact'),(66,17,'change_hostelcontact','Can change hostel contact'),(67,17,'delete_hostelcontact','Can delete hostel contact'),(68,17,'view_hostelcontact','Can view hostel contact'),(69,18,'add_lnmonline','Can add lnm online'),(70,18,'change_lnmonline','Can change lnm online'),(71,18,'delete_lnmonline','Can delete lnm online'),(72,18,'view_lnmonline','Can view lnm online');
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
  `username` varchar(17) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL,
  `email` varchar(29) DEFAULT NULL,
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$DWxOWCrlhuSn$WkbpL3gvXDgry+oY5OMCmb/PaHrTPXrPp7mCfgoI/A4=','2019-11-11',0,'Clinton','','computerscience2.10@gmail.com',1,1,'',''),(2,'pbkdf2_sha256$150000$FY45NrTnMrGX$hhLBCkB+Q5HIz74p2Di8dNZk4zW+U8LW/ggcjR4timk=','2019-11-12',1,'user','','user@g.net',1,1,'2019-11-11',''),(3,'pbkdf2_sha256$150000$HEYxSb7p6yWW$F5sAwlmeHVlg9ItWrvE5625rcGZ9t0MZygzrHEyucOw=','2019-11-11',0,'UsernameForTenant','','tenant@g.net',0,1,'2019-11-11','');
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
  `object_repr` varchar(26) DEFAULT NULL,
  `change_message` varchar(85) DEFAULT NULL,
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
INSERT INTO `django_admin_log` VALUES (1,'2019-11-11',1,'Clinton','[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,2,2),(2,'2019-11-11',1,'Vatican Cotts Hostel Plans','[{\"added\": {}}]',14,2,1),(3,'2019-11-11',1,'Vatican Cotts Hostel Plans','[{\"changed\": {\"fields\": [\"single_room_payment_price\", \"double_room_payment_price\"]}}]',14,2,2);
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
INSERT INTO `django_content_type` VALUES (11,'Profile','hostelpaymentplan'),(9,'Profile','paymentrequestheaders'),(8,'Profile','roomateselection'),(7,'Profile','tenantprofile'),(10,'Profile','userhostelplan'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(17,'landloard','hostelcontact'),(16,'landloard','hostelgallary'),(15,'landloard','hostelhomepage'),(14,'landloard','hostelplan'),(13,'landloard','hostelservice'),(12,'landloard','landlordprofile'),(18,'mpesa','lnmonline'),(6,'sessions','session');
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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-11-10'),(2,'auth','0001_initial','2019-11-10'),(3,'landloard','0001_initial','2019-11-10'),(4,'Profile','0001_initial','2019-11-10'),(5,'Profile','0002_paymentrequestheaders_timestamp','2019-11-10'),(6,'Profile','0003_userhostelplan','2019-11-10'),(7,'Profile','0004_auto_20191023_2029','2019-11-10'),(8,'Profile','0005_auto_20191023_2228','2019-11-10'),(9,'Profile','0006_auto_20191023_2245','2019-11-10'),(10,'Profile','0007_hostelpaymentplan','2019-11-10'),(11,'Profile','0008_auto_20191031_2006','2019-11-10'),(12,'Profile','0009_auto_20191031_2135','2019-11-10'),(13,'Profile','0010_auto_20191031_2137','2019-11-10'),(14,'admin','0001_initial','2019-11-10'),(15,'admin','0002_logentry_remove_auto_add','2019-11-10'),(16,'admin','0003_logentry_add_action_flag_choices','2019-11-10'),(17,'contenttypes','0002_remove_content_type_name','2019-11-10'),(18,'auth','0002_alter_permission_name_max_length','2019-11-10'),(19,'auth','0003_alter_user_email_max_length','2019-11-10'),(20,'auth','0004_alter_user_username_opts','2019-11-10'),(21,'auth','0005_alter_user_last_login_null','2019-11-10'),(22,'auth','0006_require_contenttypes_0002','2019-11-10'),(23,'auth','0007_alter_validators_add_error_messages','2019-11-10'),(24,'auth','0008_alter_user_username_max_length','2019-11-10'),(25,'auth','0009_alter_user_last_name_max_length','2019-11-10'),(26,'auth','0010_alter_group_name_max_length','2019-11-10'),(27,'auth','0011_update_proxy_permissions','2019-11-10'),(28,'mpesa','0001_initial','2019-11-10'),(29,'sessions','0001_initial','2019-11-10');
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
INSERT INTO `django_session` VALUES ('rt7sjq9fi8sxswmzzu57udojdltea6ax','MjM3Y2E0N2ZhNTU3YTEzMDMxOGM1MTI1M2YxNTUyOTg1YjQ3ODMzMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMWIxNjY2ODg4NDAyMWQxYjlkOWZlYjA3YzFhMjZhMjVjMjg1Nzg2In0=','2019-11-25');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelcontact`
--

DROP TABLE IF EXISTS `landloard_hostelcontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelcontact` (
  `id` tinyint(4) DEFAULT NULL,
  `hostel_phone_number` bigint(20) DEFAULT NULL,
  `hostel_mail` varchar(11) DEFAULT NULL,
  `payment_method` varchar(6) DEFAULT NULL,
  `hostel_address` text,
  `hostel_name_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelcontact`
--

LOCK TABLES `landloard_hostelcontact` WRITE;
/*!40000 ALTER TABLE `landloard_hostelcontact` DISABLE KEYS */;
INSERT INTO `landloard_hostelcontact` VALUES (1,797328328,'toast@g.net','M-Pesa','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?',1);
/*!40000 ALTER TABLE `landloard_hostelcontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelgallary`
--

DROP TABLE IF EXISTS `landloard_hostelgallary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelgallary` (
  `id` tinyint(4) DEFAULT NULL,
  `photo_description` text,
  `photo` varchar(55) DEFAULT NULL,
  `hostel_name_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelgallary`
--

LOCK TABLES `landloard_hostelgallary` WRITE;
/*!40000 ALTER TABLE `landloard_hostelgallary` DISABLE KEYS */;
INSERT INTO `landloard_hostelgallary` VALUES (1,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','Hostel_gallery/apartment-bed-bedroom-462235_o42Trrh.jpg',1),(2,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','Hostel_gallery/bed-bedroom-bright-916337_Zp0WhIH.jpg',1);
/*!40000 ALTER TABLE `landloard_hostelgallary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelhomepage`
--

DROP TABLE IF EXISTS `landloard_hostelhomepage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelhomepage` (
  `id` tinyint(4) DEFAULT NULL,
  `welcoming_message` text,
  `background_image` varchar(57) DEFAULT NULL,
  `hostel_name_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelhomepage`
--

LOCK TABLES `landloard_hostelhomepage` WRITE;
/*!40000 ALTER TABLE `landloard_hostelhomepage` DISABLE KEYS */;
INSERT INTO `landloard_hostelhomepage` VALUES (1,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','hostel_homepages/apartment-bed-bedroom-271624_m6GyAhB.jpg',1);
/*!40000 ALTER TABLE `landloard_hostelhomepage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelplan`
--

DROP TABLE IF EXISTS `landloard_hostelplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelplan` (
  `id` tinyint(4) DEFAULT NULL,
  `single_room_desc` text,
  `single_room_payment_price` mediumint(9) DEFAULT NULL,
  `double_room_payment_price` smallint(6) DEFAULT NULL,
  `double_room_desc` text,
  `self_contained` varchar(4) DEFAULT NULL,
  `mpesa_shotcode` mediumint(9) DEFAULT NULL,
  `self_contained_payment_price` varchar(4) DEFAULT NULL,
  `hostel_name_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelplan`
--

LOCK TABLES `landloard_hostelplan` WRITE;
/*!40000 ALTER TABLE `landloard_hostelplan` DISABLE KEYS */;
INSERT INTO `landloard_hostelplan` VALUES (1,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?',16000,6000,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','None',612226,'None',1);
/*!40000 ALTER TABLE `landloard_hostelplan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `landloard_hostelservice`
--

DROP TABLE IF EXISTS `landloard_hostelservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `landloard_hostelservice` (
  `id` tinyint(4) DEFAULT NULL,
  `security` text,
  `water_supply` text,
  `power_supply` text,
  `bed_size` text,
  `room_size` text,
  `table_and_chair_availabitity` text,
  `total_no_of_rooms` tinyint(4) DEFAULT NULL,
  `hostel_name_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_hostelservice`
--

LOCK TABLES `landloard_hostelservice` WRITE;
/*!40000 ALTER TABLE `landloard_hostelservice` DISABLE KEYS */;
INSERT INTO `landloard_hostelservice` VALUES (1,'his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?','his Mercury transit will be visible, weather permitting, for several hours in most of the world, including the US, South America, Africa, and Europe.\r\n\r\nWe are standing by to LIVE Stream the Mercury transit if the weather conditions are favorable.\r\n\r\nIs this Mercury Transit visible in Lusaka?',40,1);
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
  `your_full_name` varchar(12) DEFAULT NULL,
  `your_phone_number` bigint(20) DEFAULT NULL,
  `your_picture` varchar(42) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landloard_landlordprofile`
--

LOCK TABLES `landloard_landlordprofile` WRITE;
/*!40000 ALTER TABLE `landloard_landlordprofile` DISABLE KEYS */;
INSERT INTO `landloard_landlordprofile` VALUES (1,'Vatican Cotts','Rongo University','Clinton Agoo',798305230,'landlord/apartment-bed-bedding-1034584.jpg','2019-11-11',1);
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
  `merchant_request_id` varchar(0) DEFAULT NULL,
  `checkout_request_id` varchar(0) DEFAULT NULL,
  `result_code` varchar(0) DEFAULT NULL,
  `result_description` varchar(0) DEFAULT NULL,
  `saccess_amount` varchar(0) DEFAULT NULL,
  `saccess_mpesa_receipt_number` varchar(0) DEFAULT NULL,
  `saccess_transaction_date` varchar(0) DEFAULT NULL,
  `saccess_balance` varchar(0) DEFAULT NULL,
  `saccess_phone_number` varchar(0) DEFAULT NULL,
  `success_result_description` varchar(0) DEFAULT NULL,
  `fail_result_description` varchar(0) DEFAULT NULL,
  `fail_merchant_request_id` varchar(0) DEFAULT NULL,
  `fail_result_code` varchar(0) DEFAULT NULL
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
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',29),('Profile_paymentrequestheaders',2),('Profile_userhostelplan',1),('Profile_hostelpaymentplan',1),('Profile_roomateselection',0),('django_admin_log',3),('django_content_type',18),('auth_permission',72),('auth_user',3),('auth_group',0),('landloard_landlordprofile',1),('landloard_hostelhomepage',1),('landloard_hostelservice',1),('landloard_hostelcontact',1),('landloard_hostelgallary',2),('Profile_tenantprofile',1),('landloard_hostelplan',1);
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

-- Dump completed on 2019-08-22 15:20:31
