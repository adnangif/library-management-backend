use lib;


-- Inserting book 1
INSERT INTO book_info (info_id, title, author, description, publication_year, edition)
VALUES (10, 'Introduction to Algorithms', 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein', 'A comprehensive introduction to algorithms and data structures', 1990, 'Third edition');

-- Inserting book 2
INSERT INTO book_info (info_id, title, author, description, publication_year, edition)
VALUES (11, 'Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', 'Provides guidelines for writing clean, maintainable code', 2008, 'First edition');

-- Inserting book 3
INSERT INTO book_info (info_id, title, author, description, publication_year, edition)
VALUES (12, 'Operating System Concepts', 'Abraham Silberschatz, Peter B. Galvin, Greg Gagne', 'Covers fundamental concepts of operating systems', 2008, 'Eighth edition');

-- Inserting book 4
INSERT INTO book_info (info_id, title, author, description, publication_year, edition)
VALUES (13, 'Computer Networking: A Top-Down Approach', 'James F. Kurose, Keith W. Ross', 'Covers principles of computer networking from application to network layers', 2017, 'Seventh edition');

-- Inserting book 5
INSERT INTO book_info (info_id, title, author, description, publication_year, edition)
VALUES (14, 'Design Patterns: Elements of Reusable Object-Oriented Software', 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'Introduces design patterns in software engineering', 1994, 'First edition');

-- Inserting 15 rows into book_copy table 
INSERT INTO book_copy (info_id, book_id, is_available)
VALUES 
    (10, 1, 1),
    (11, 2, 1),
    (12, 3, 1),
    (13, 4, 1),
    (14, 5, 1),
    (13, 6, 1),
    (10, 7, 1),
    (11, 8, 1),
    (12, 9, 1),
    (13, 10, 1),
    (14, 11, 1),
    (14, 12, 1),
    (10, 13, 1),
    (11, 14, 1),
    (12, 15, 1);

-- Inserting categories for book 1
INSERT INTO book_category (info_id, category)
VALUES (10, 'Computer Science');

-- Inserting categories for book 2
INSERT INTO book_category (info_id, category)
VALUES (11, 'Computer Science');

-- Inserting categories for book 3
INSERT INTO book_category (info_id, category)
VALUES (12, 'Computer Science');

-- Inserting categories for book 4
INSERT INTO book_category (info_id, category)
VALUES (13, 'Computer Science');

-- Inserting categories for book 5
INSERT INTO book_category (info_id, category)
VALUES (14, 'Computer Science');


-- user
INSERT INTO `user`(`user_id`,`institution_id_number`,`first_name`,`last_name`,`hashed_pass`,`email`,`phone`) 
VALUES
(1,2101,'rahad','tithi','123','2101@gmail.com','01234567809'),
(2,2102,'partho','susmi','123','2102@gmail.com','01244469789'),
(3,2103,'rabby','fahim','123','2103@gmail.com','01236354789'),
(4,2104,'banhi','tithi','123','2104@gmail.com','01232384789'),
(5,2105,'arnob','aaru','123','2105@gmail.com','01238576789'),
(6,2106,'antu','ghum','123','2106@gmail.com','01227876789');

-- order
INSERT INTO `order`(`order_id`,`user_id`,`issue_datetime`,`due_datetime`,`last_collection_time`) 
VALUES
(1,1,'2023-01-25 00:00:00',190,3),
(2,1,'2023-01-25 00:00:00',190,3),
(3,3,'2023-02-5 00:00:00',190,3),
(4,6,'2023-03-15 00:00:00',190,3),
(5,4,'2023-01-5 00:00:00',190,3),
(6,2,'2023-01-2 00:00:00',190,3),
(7,5,'2023-01-21 00:00:00',190,3);

-- borrowed_book
INSERT INTO `ordered_book`(`order_id`,`book_id`)
VALUES
(1,2),
(2,6),
(3,7),
(4,1),
(5,5),
(6,9),
(7,3);
