CREATE SCHEMA lib;
USE lib;

CREATE TABLE `book_info` (
  `info_id` integer PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `author` varchar(200) NOT NULL,
  `description` varchar(500),
  `publication_year` integer,
  `edition` varchar(50)
);

CREATE TABLE `book_copy` (
  `info_id` integer NOT NULL,
  `book_id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `is_available` integer NOT NULL DEFAULT 1
);

CREATE TABLE `book_category` (
  `info_id` integer NOT NULL,
  `category` varchar(200) NOT NULL
);

CREATE TABLE `user` (
  `user_id` integer PRIMARY KEY AUTO_INCREMENT,
  `institution_id_number` integer UNIQUE NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200),
  `hashed_pass` varchar(300) NOT NULL,
  `email` varchar(300) UNIQUE NOT NULL,
  `phone` varchar(100) NOT NULL,
  `is_maintainer` smallint NOT NULL DEFAULT 0
);

CREATE TABLE `order` (
  `order_id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `issue_datetime` datetime DEFAULT current_timestamp(),
  `due_datetime` datetime NOT NULL,
  `last_collection_time` datetime NOT NULL
);

CREATE TABLE `ordered_book` (
  `order_id` integer NOT NULL,
  `book_id` integer NOT NULL
);

CREATE TABLE `borrow_record` (
  `borrow_id` integer PRIMARY KEY AUTO_INCREMENT,
  `collection_date` datetime DEFAULT current_timestamp(),
  `order_id` integer NOT NULL,
  `delivered_by` integer NOT NULL
);

CREATE TABLE `borrowed_book` (
  `book_id` integer NOT NULL,
  `borrow_id` integer NOT NULL
);

CREATE TABLE `return_record` (
  `return_id` integer PRIMARY KEY AUTO_INCREMENT,
  `book_return_date` datetime DEFAULT current_timestamp(),
  `order_id` integer NOT NULL,
  `return_to` integer NOT NULL
);

CREATE TABLE `returned_book` (
  `return_id` integer NOT NULL,
  `book_id` integer NOT NULL
);

ALTER TABLE `book_copy` ADD FOREIGN KEY (`info_id`) REFERENCES `book_info` (`info_id`);

ALTER TABLE `book_category` ADD FOREIGN KEY (`info_id`) REFERENCES `book_info` (`info_id`);

ALTER TABLE `order` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

ALTER TABLE `ordered_book` ADD FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`);

ALTER TABLE `ordered_book` ADD FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`);

ALTER TABLE `borrow_record` ADD FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`);

ALTER TABLE `borrow_record` ADD FOREIGN KEY (`delivered_by`) REFERENCES `user` (`user_id`);

ALTER TABLE `borrowed_book` ADD FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`);

ALTER TABLE `borrowed_book` ADD FOREIGN KEY (`borrow_id`) REFERENCES `borrow_record` (`borrow_id`);

ALTER TABLE `return_record` ADD FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`);

ALTER TABLE `return_record` ADD FOREIGN KEY (`return_to`) REFERENCES `user` (`user_id`);

ALTER TABLE `returned_book` ADD FOREIGN KEY (`return_id`) REFERENCES `return_record` (`return_id`);

ALTER TABLE `returned_book` ADD FOREIGN KEY (`book_id`) REFERENCES `book_copy` (`book_id`);
