-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2025 at 11:45 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ddms_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Designation', 7, 'add_designation'),
(26, 'Can change Designation', 7, 'change_designation'),
(27, 'Can delete Designation', 7, 'delete_designation'),
(28, 'Can view Designation', 7, 'view_designation'),
(29, 'Can add Division', 8, 'add_division'),
(30, 'Can change Division', 8, 'change_division'),
(31, 'Can delete Division', 8, 'delete_division'),
(32, 'Can view Division', 8, 'view_division'),
(33, 'Can add Organization', 9, 'add_organization'),
(34, 'Can change Organization', 9, 'change_organization'),
(35, 'Can delete Organization', 9, 'delete_organization'),
(36, 'Can view Organization', 9, 'view_organization'),
(37, 'Can add Organization Category', 10, 'add_organizationcategory'),
(38, 'Can change Organization Category', 10, 'change_organizationcategory'),
(39, 'Can delete Organization Category', 10, 'delete_organizationcategory'),
(40, 'Can view Organization Category', 10, 'view_organizationcategory'),
(41, 'Can add Person Level', 11, 'add_personlevel'),
(42, 'Can change Person Level', 11, 'change_personlevel'),
(43, 'Can delete Person Level', 11, 'delete_personlevel'),
(44, 'Can view Person Level', 11, 'view_personlevel'),
(45, 'Can add Person', 12, 'add_personlist'),
(46, 'Can change Person', 12, 'change_personlist'),
(47, 'Can delete Person', 12, 'delete_personlist'),
(48, 'Can view Person', 12, 'view_personlist'),
(49, 'Can add Set SMS List', 13, 'add_sentsmslist'),
(50, 'Can change Set SMS List', 13, 'change_sentsmslist'),
(51, 'Can delete Set SMS List', 13, 'delete_sentsmslist'),
(52, 'Can view Set SMS List', 13, 'view_sentsmslist'),
(53, 'Can add Person Follow-Up', 14, 'add_personfollowup'),
(54, 'Can change Person Follow-Up', 14, 'change_personfollowup'),
(55, 'Can delete Person Follow-Up', 14, 'delete_personfollowup'),
(56, 'Can view Person Follow-Up', 14, 'view_personfollowup'),
(57, 'Can add Organization Follow-Up', 15, 'add_organizationfollowup'),
(58, 'Can change Organization Follow-Up', 15, 'change_organizationfollowup'),
(59, 'Can delete Organization Follow-Up', 15, 'delete_organizationfollowup'),
(60, 'Can view Organization Follow-Up', 15, 'view_organizationfollowup'),
(61, 'Can add Marketing Activity', 16, 'add_marketingactivity'),
(62, 'Can change Marketing Activity', 16, 'change_marketingactivity'),
(63, 'Can delete Marketing Activity', 16, 'delete_marketingactivity'),
(64, 'Can view Marketing Activity', 16, 'view_marketingactivity'),
(65, 'Can add Company', 17, 'add_companylist'),
(66, 'Can change Company', 17, 'change_companylist'),
(67, 'Can delete Company', 17, 'delete_companylist'),
(68, 'Can view Company', 17, 'view_companylist'),
(69, 'Can add Bulk Email', 18, 'add_bulkemail'),
(70, 'Can change Bulk Email', 18, 'change_bulkemail'),
(71, 'Can delete Bulk Email', 18, 'delete_bulkemail'),
(72, 'Can view Bulk Email', 18, 'view_bulkemail');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bulk_email`
--

CREATE TABLE `bulk_email` (
  `id` bigint(20) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `sent_date` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `rank` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `company_list`
--

CREATE TABLE `company_list` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `mobile1` varchar(30) DEFAULT NULL,
  `mobile2` varchar(30) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `map_location` longtext DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `division_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `designation`
--

CREATE TABLE `designation` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `rank` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `designation`
--

INSERT INTO `designation` (`id`, `name`, `rank`, `created`, `updated`) VALUES
(1, 'Software Engineer', 1, '2025-04-12 14:20:10.199827', '2025-04-12 14:20:10.200408'),
(2, 'Founder', 1, '2025-04-12 14:42:12.708328', '2025-04-12 14:42:12.708328');

-- --------------------------------------------------------

--
-- Table structure for table `division`
--

CREATE TABLE `division` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext DEFAULT NULL,
  `rank` int(11) NOT NULL,
  `color` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `division`
--

INSERT INTO `division` (`id`, `name`, `description`, `rank`, `color`, `created`, `updated`) VALUES
(1, 'Dhaka', 'asdfa ', 1, 'green', '2025-04-12 14:33:41.793176', '2025-04-12 14:33:41.793176'),
(2, 'Rajshahi', 'segwerrg', 4, 'green', '2025-04-14 07:53:13.281766', '2025-04-14 07:53:13.281766');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(18, 'directory_app', 'bulkemail'),
(17, 'directory_app', 'companylist'),
(7, 'directory_app', 'designation'),
(8, 'directory_app', 'division'),
(16, 'directory_app', 'marketingactivity'),
(9, 'directory_app', 'organization'),
(10, 'directory_app', 'organizationcategory'),
(15, 'directory_app', 'organizationfollowup'),
(14, 'directory_app', 'personfollowup'),
(11, 'directory_app', 'personlevel'),
(12, 'directory_app', 'personlist'),
(13, 'directory_app', 'sentsmslist'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-04-12 14:18:25.888160'),
(2, 'auth', '0001_initial', '2025-04-12 14:18:26.833146'),
(3, 'admin', '0001_initial', '2025-04-12 14:18:27.184341'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-04-12 14:18:27.200298'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-04-12 14:18:27.212909'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-04-12 14:18:27.348179'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-04-12 14:18:27.467812'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-04-12 14:18:27.502720'),
(9, 'auth', '0004_alter_user_username_opts', '2025-04-12 14:18:27.529323'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-04-12 14:18:27.654046'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-04-12 14:18:27.662597'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-04-12 14:18:27.679491'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-04-12 14:18:27.704393'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-04-12 14:18:27.785623'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-04-12 14:18:27.828686'),
(16, 'auth', '0011_update_proxy_permissions', '2025-04-12 14:18:27.854093'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-04-12 14:18:27.878334'),
(18, 'directory_app', '0001_initial', '2025-04-12 14:18:29.485657'),
(19, 'sessions', '0001_initial', '2025-04-12 14:18:29.546865'),
(20, 'directory_app', '0002_organization_division', '2025-04-12 14:34:29.378924');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `marketing_activity`
--

CREATE TABLE `marketing_activity` (
  `id` bigint(20) NOT NULL,
  `activity_type` varchar(50) NOT NULL,
  `activity_details` longtext NOT NULL,
  `activity_date` datetime(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `organization`
--

CREATE TABLE `organization` (
  `id` bigint(20) NOT NULL,
  `org_name` varchar(255) NOT NULL,
  `contact_person_name` varchar(255) NOT NULL,
  `email1` varchar(255) NOT NULL,
  `email2` varchar(255) NOT NULL,
  `email3` varchar(255) NOT NULL,
  `mobile1` varchar(30) DEFAULT NULL,
  `mobile2` varchar(30) DEFAULT NULL,
  `mobile3` varchar(30) DEFAULT NULL,
  `residential_address` longtext DEFAULT NULL,
  `office_address` longtext DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `social_facebook` varchar(200) DEFAULT NULL,
  `social_linkedin` varchar(200) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `designation_id` bigint(20) NOT NULL,
  `division_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `organization`
--

INSERT INTO `organization` (`id`, `org_name`, `contact_person_name`, `email1`, `email2`, `email3`, `mobile1`, `mobile2`, `mobile3`, `residential_address`, `office_address`, `website`, `social_facebook`, `social_linkedin`, `notes`, `created`, `updated`, `category_id`, `designation_id`, `division_id`) VALUES
(1, 'Somadhan IT Limited', 'Md. Akkas Mia', 'akkas@gmail.com', 'akkas2@gmail.com', 'akkas3@gmail.com', '1234', '123444', '12342345', 'asd f', 'asd f', 'https://somadhanit.com/', 'https://somadhanit.com/', 'https://somadhanit.com/', ' asdf', '2025-04-12 14:23:40.894958', '2025-04-12 14:23:40.894958', 1, 1, 1),
(2, 'MM AGRO', 'Omar Faruk - Test', 'faruk@omar.com', 'faruk@omar.com', 'faruk@omar.com', '7652389008', '7652389008', '7652389008', 'ST road', '775 waterville drive', 'https://somadhanit.com/', 'https://somadhanit.com/', 'https://somadhanit.com/', 'Nai khali', '2025-04-12 14:44:44.085755', '2025-04-12 14:44:44.085755', 1, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `organization_category`
--

CREATE TABLE `organization_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext DEFAULT NULL,
  `rank` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `organization_category`
--

INSERT INTO `organization_category` (`id`, `name`, `description`, `rank`, `created`, `updated`) VALUES
(1, 'Limited Company', 'Limited Company', 1, '2025-04-12 14:20:32.184274', '2025-04-12 14:20:32.184274'),
(2, 'Organic', 'Organic', 1, '2025-04-12 14:41:58.759170', '2025-04-12 14:41:58.759170');

-- --------------------------------------------------------

--
-- Table structure for table `organization_follow_up`
--

CREATE TABLE `organization_follow_up` (
  `id` bigint(20) NOT NULL,
  `follow_up_date` datetime(6) NOT NULL,
  `status` varchar(255) NOT NULL,
  `comments` longtext DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `organization_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `person_follow_up`
--

CREATE TABLE `person_follow_up` (
  `id` bigint(20) NOT NULL,
  `follow_up_date` datetime(6) NOT NULL,
  `status` varchar(255) NOT NULL,
  `comments` longtext DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `person_level`
--

CREATE TABLE `person_level` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `rank` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `person_level`
--

INSERT INTO `person_level` (`id`, `name`, `rank`, `created`, `updated`) VALUES
(1, 'A1', 1, '2025-04-12 14:42:25.294967', '2025-04-12 14:42:25.294967');

-- --------------------------------------------------------

--
-- Table structure for table `person_list`
--

CREATE TABLE `person_list` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `whatsapp` varchar(20) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `profile_details` longtext DEFAULT NULL,
  `rank` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `designation_id` bigint(20) NOT NULL,
  `organization_id` bigint(20) NOT NULL,
  `person_level_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sent_sms_list`
--

CREATE TABLE `sent_sms_list` (
  `id` bigint(20) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `message` longtext NOT NULL,
  `sent_date` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created` datetime(6) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bulk_email`
--
ALTER TABLE `bulk_email`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bulk_email_person_id_d9647d97_fk_person_list_id` (`person_id`);

--
-- Indexes for table `company_list`
--
ALTER TABLE `company_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `company_list_category_id_4096ca95_fk_organization_category_id` (`category_id`),
  ADD KEY `company_list_division_id_00d8a6c5_fk_division_id` (`division_id`);

--
-- Indexes for table `designation`
--
ALTER TABLE `designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `division`
--
ALTER TABLE `division`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `marketing_activity`
--
ALTER TABLE `marketing_activity`
  ADD PRIMARY KEY (`id`),
  ADD KEY `marketing_activity_person_id_10fc8585_fk_person_list_id` (`person_id`);

--
-- Indexes for table `organization`
--
ALTER TABLE `organization`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `contact_person_name` (`contact_person_name`),
  ADD UNIQUE KEY `email1` (`email1`),
  ADD UNIQUE KEY `email2` (`email2`),
  ADD UNIQUE KEY `email3` (`email3`),
  ADD KEY `organization_category_id_d88e50fd_fk_organization_category_id` (`category_id`),
  ADD KEY `organization_designation_id_90ed5238_fk_designation_id` (`designation_id`),
  ADD KEY `organization_division_id_778b15a7_fk_division_id` (`division_id`);

--
-- Indexes for table `organization_category`
--
ALTER TABLE `organization_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `organization_follow_up`
--
ALTER TABLE `organization_follow_up`
  ADD PRIMARY KEY (`id`),
  ADD KEY `organization_follow__organization_id_530ff500_fk_organizat` (`organization_id`);

--
-- Indexes for table `person_follow_up`
--
ALTER TABLE `person_follow_up`
  ADD PRIMARY KEY (`id`),
  ADD KEY `person_follow_up_person_id_9dfd299c_fk_person_list_id` (`person_id`);

--
-- Indexes for table `person_level`
--
ALTER TABLE `person_level`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `person_list`
--
ALTER TABLE `person_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `person_list_designation_id_9bdaed9d_fk_designation_id` (`designation_id`),
  ADD KEY `person_list_organization_id_a8b32337_fk_organization_id` (`organization_id`),
  ADD KEY `person_list_person_level_id_629601ea_fk_person_level_id` (`person_level_id`);

--
-- Indexes for table `sent_sms_list`
--
ALTER TABLE `sent_sms_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sent_sms_list_person_id_fa935de1_fk_person_list_id` (`person_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bulk_email`
--
ALTER TABLE `bulk_email`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `company_list`
--
ALTER TABLE `company_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `designation`
--
ALTER TABLE `designation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `division`
--
ALTER TABLE `division`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `marketing_activity`
--
ALTER TABLE `marketing_activity`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `organization`
--
ALTER TABLE `organization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `organization_category`
--
ALTER TABLE `organization_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `organization_follow_up`
--
ALTER TABLE `organization_follow_up`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `person_follow_up`
--
ALTER TABLE `person_follow_up`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `person_level`
--
ALTER TABLE `person_level`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `person_list`
--
ALTER TABLE `person_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sent_sms_list`
--
ALTER TABLE `sent_sms_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `bulk_email`
--
ALTER TABLE `bulk_email`
  ADD CONSTRAINT `bulk_email_person_id_d9647d97_fk_person_list_id` FOREIGN KEY (`person_id`) REFERENCES `person_list` (`id`);

--
-- Constraints for table `company_list`
--
ALTER TABLE `company_list`
  ADD CONSTRAINT `company_list_category_id_4096ca95_fk_organization_category_id` FOREIGN KEY (`category_id`) REFERENCES `organization_category` (`id`),
  ADD CONSTRAINT `company_list_division_id_00d8a6c5_fk_division_id` FOREIGN KEY (`division_id`) REFERENCES `division` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `marketing_activity`
--
ALTER TABLE `marketing_activity`
  ADD CONSTRAINT `marketing_activity_person_id_10fc8585_fk_person_list_id` FOREIGN KEY (`person_id`) REFERENCES `person_list` (`id`);

--
-- Constraints for table `organization`
--
ALTER TABLE `organization`
  ADD CONSTRAINT `organization_category_id_d88e50fd_fk_organization_category_id` FOREIGN KEY (`category_id`) REFERENCES `organization_category` (`id`),
  ADD CONSTRAINT `organization_designation_id_90ed5238_fk_designation_id` FOREIGN KEY (`designation_id`) REFERENCES `designation` (`id`),
  ADD CONSTRAINT `organization_division_id_778b15a7_fk_division_id` FOREIGN KEY (`division_id`) REFERENCES `division` (`id`);

--
-- Constraints for table `organization_follow_up`
--
ALTER TABLE `organization_follow_up`
  ADD CONSTRAINT `organization_follow__organization_id_530ff500_fk_organizat` FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`);

--
-- Constraints for table `person_follow_up`
--
ALTER TABLE `person_follow_up`
  ADD CONSTRAINT `person_follow_up_person_id_9dfd299c_fk_person_list_id` FOREIGN KEY (`person_id`) REFERENCES `person_list` (`id`);

--
-- Constraints for table `person_list`
--
ALTER TABLE `person_list`
  ADD CONSTRAINT `person_list_designation_id_9bdaed9d_fk_designation_id` FOREIGN KEY (`designation_id`) REFERENCES `designation` (`id`),
  ADD CONSTRAINT `person_list_organization_id_a8b32337_fk_organization_id` FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`),
  ADD CONSTRAINT `person_list_person_level_id_629601ea_fk_person_level_id` FOREIGN KEY (`person_level_id`) REFERENCES `person_level` (`id`);

--
-- Constraints for table `sent_sms_list`
--
ALTER TABLE `sent_sms_list`
  ADD CONSTRAINT `sent_sms_list_person_id_fa935de1_fk_person_list_id` FOREIGN KEY (`person_id`) REFERENCES `person_list` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
