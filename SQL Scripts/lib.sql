-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 16, 2024 at 02:25 AM
-- Server version: 10.11.6-MariaDB-0+deb12u1
-- PHP Version: 8.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lib`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_category`
--

CREATE TABLE `book_category` (
  `info_id` int(11) NOT NULL,
  `category` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book_category`
--

INSERT INTO `book_category` (`info_id`, `category`) VALUES
(11, 'Computer Science'),
(12, 'Computer Science'),
(13, 'Computer Science'),
(14, 'Computer Science');

-- --------------------------------------------------------

--
-- Table structure for table `book_copy`
--

CREATE TABLE `book_copy` (
  `info_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `is_available` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book_copy`
--

INSERT INTO `book_copy` (`info_id`, `book_id`, `is_available`) VALUES
(11, 2, 0),
(12, 3, 0),
(13, 4, 0),
(14, 5, 0),
(13, 6, 0),
(11, 8, 1),
(12, 9, 1),
(13, 10, 1),
(14, 11, 1),
(14, 12, 1),
(11, 14, 1),
(12, 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `book_info`
--

CREATE TABLE `book_info` (
  `info_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `author` varchar(200) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `publication_year` int(11) DEFAULT NULL,
  `edition` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book_info`
--

INSERT INTO `book_info` (`info_id`, `title`, `author`, `description`, `publication_year`, `edition`) VALUES
(11, 'Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', 'Provides guidelines for writing clean, maintainable code', 2008, 'First edition'),
(12, 'Operating System Concepts', 'Abraham Silberschatz, Peter B. Galvin, Greg Gagne', 'Covers fundamental concepts of operating systems', 2008, 'Eighth edition'),
(13, 'Computer Networking: A Top-Down Approach', 'James F. Kurose, Keith W. Ross', 'Covers principles of computer networking from application to network layers', 2017, 'Seventh edition'),
(14, 'Design Patterns: Elements of Reusable Object-Oriented Software', 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'Introduces design patterns in software engineering', 1994, 'First edition');

-- --------------------------------------------------------

--
-- Table structure for table `borrowed_book`
--

CREATE TABLE `borrowed_book` (
  `book_id` int(11) NOT NULL,
  `borrow_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `borrow_record`
--

CREATE TABLE `borrow_record` (
  `borrow_id` int(11) NOT NULL,
  `collection_date` datetime DEFAULT current_timestamp(),
  `order_id` int(11) NOT NULL,
  `delivered_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE `librarian` (
  `librarian_id` int(11) NOT NULL,
  `institution_id_number` int(11) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `hashed_pass` varchar(400) NOT NULL,
  `email` varchar(300) NOT NULL,
  `phone` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `issue_datetime` datetime DEFAULT current_timestamp(),
  `due_datetime` int(11) NOT NULL,
  `last_collection_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`order_id`, `user_id`, `issue_datetime`, `due_datetime`, `last_collection_time`) VALUES
(6, 1, '2024-04-15 12:07:04', 180, 5),
(10, 1, '2024-04-15 13:37:15', 180, 5);

-- --------------------------------------------------------

--
-- Table structure for table `ordered_book`
--

CREATE TABLE `ordered_book` (
  `order_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ordered_book`
--

INSERT INTO `ordered_book` (`order_id`, `book_id`) VALUES
(10, 2),
(10, 3),
(10, 4),
(6, 5),
(6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `returned_book`
--

CREATE TABLE `returned_book` (
  `book_id` int(11) NOT NULL,
  `return_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `return_record`
--

CREATE TABLE `return_record` (
  `return_id` int(11) NOT NULL,
  `book_return_date` datetime DEFAULT current_timestamp(),
  `order_id` int(11) NOT NULL,
  `return_to` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `institution_id_number` int(11) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `hashed_pass` varchar(400) NOT NULL,
  `email` varchar(300) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `institution_id_number`, `first_name`, `last_name`, `hashed_pass`, `email`, `phone`) VALUES
(1, 342367, 'alib', 'babab', 'pbkdf2_sha256$720000$a75a89b9440d12553043d9bee206e8a040bb71f8c4ca4e4636f33b039a503ba6$65mUZGRW/nw6kWUBYnSBESvKLr5uvA0NhpCqsnQ+3zk=', 'basdfr43@gmail.com', '34422332');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book_category`
--
ALTER TABLE `book_category`
  ADD KEY `book_category_ibfk_1` (`info_id`);

--
-- Indexes for table `book_copy`
--
ALTER TABLE `book_copy`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `book_copy_ibfk_1` (`info_id`);

--
-- Indexes for table `book_info`
--
ALTER TABLE `book_info`
  ADD PRIMARY KEY (`info_id`);

--
-- Indexes for table `borrowed_book`
--
ALTER TABLE `borrowed_book`
  ADD KEY `book_id` (`book_id`),
  ADD KEY `borrow_id` (`borrow_id`);

--
-- Indexes for table `borrow_record`
--
ALTER TABLE `borrow_record`
  ADD PRIMARY KEY (`borrow_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `delivered_by` (`delivered_by`);

--
-- Indexes for table `librarian`
--
ALTER TABLE `librarian`
  ADD PRIMARY KEY (`librarian_id`),
  ADD UNIQUE KEY `institution_id_number` (`institution_id_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `ordered_book`
--
ALTER TABLE `ordered_book`
  ADD KEY `order_id` (`order_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `returned_book`
--
ALTER TABLE `returned_book`
  ADD KEY `book_id` (`book_id`),
  ADD KEY `return_id` (`return_id`);

--
-- Indexes for table `return_record`
--
ALTER TABLE `return_record`
  ADD PRIMARY KEY (`return_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `return_to` (`return_to`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `institution_id_number` (`institution_id_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book_copy`
--
ALTER TABLE `book_copy`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `book_info`
--
ALTER TABLE `book_info`
  MODIFY `info_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `borrow_record`
--
ALTER TABLE `borrow_record`
  MODIFY `borrow_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `librarian`
--
ALTER TABLE `librarian`
  MODIFY `librarian_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `return_record`
--
ALTER TABLE `return_record`
  MODIFY `return_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book_category`
--
ALTER TABLE `book_category`
  ADD CONSTRAINT `book_category_ibfk_1` FOREIGN KEY (`info_id`) REFERENCES `book_info` (`info_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `book_copy`
--
ALTER TABLE `book_copy`
  ADD CONSTRAINT `book_copy_ibfk_1` FOREIGN KEY (`info_id`) REFERENCES `book_info` (`info_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `borrowed_book`
--
ALTER TABLE `borrowed_book`
  ADD CONSTRAINT `borrowed_book_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`),
  ADD CONSTRAINT `borrowed_book_ibfk_2` FOREIGN KEY (`borrow_id`) REFERENCES `borrow_record` (`borrow_id`);

--
-- Constraints for table `borrow_record`
--
ALTER TABLE `borrow_record`
  ADD CONSTRAINT `borrow_record_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `borrow_record_ibfk_2` FOREIGN KEY (`delivered_by`) REFERENCES `librarian` (`librarian_id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `ordered_book`
--
ALTER TABLE `ordered_book`
  ADD CONSTRAINT `ordered_book_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `ordered_book_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`);

--
-- Constraints for table `returned_book`
--
ALTER TABLE `returned_book`
  ADD CONSTRAINT `returned_book_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`),
  ADD CONSTRAINT `returned_book_ibfk_2` FOREIGN KEY (`return_id`) REFERENCES `return_record` (`return_id`);

--
-- Constraints for table `return_record`
--
ALTER TABLE `return_record`
  ADD CONSTRAINT `return_record_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `return_record_ibfk_2` FOREIGN KEY (`return_to`) REFERENCES `librarian` (`librarian_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
