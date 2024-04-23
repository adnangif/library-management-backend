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


-- NEW DATA

-- Inserting data values for books into the book_info table
INSERT INTO `book_info`(`info_id`,`title`,`author`,`description`,`publication_year`,`edition`)
VALUES
    (15, 'Introduction to Algorithms', 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein', 'A comprehensive guide to algorithms and their analysis.', 2009, 3),
    (16, 'Engineering Mechanics: Dynamics', 'J.L. Meriam, L.G. Kraige', 'A textbook covering the principles of dynamics in engineering mechanics.', 2016, 8),
    (17, 'Fundamentals of Electric Circuits', 'Charles K. Alexander, Matthew N.O. Sadiku', 'An introductory text on electric circuits, covering basic principles and analysis techniques.', 2013, 5),
    (18, 'Structural Analysis', 'Russell C. Hibbeler', 'A textbook on the analysis of structures and structural components.', 2017, 10),
    (19, 'Digital Design', 'M. Morris Mano, Michael D. Ciletti', 'A comprehensive textbook covering digital logic design and computer architecture.', 2014, 6),
    (20, 'Engineering Electromagnetics', 'William H. Hayt Jr., John A. Buck', 'An introduction to electromagnetics with engineering applications.', 2011, 8),
    (21, 'Mechanical Engineering Design', 'Joseph E. Shigley, Charles R. Mischke, Richard G. Budynas', 'A textbook covering the principles and practices of mechanical engineering design.', 2014, 10),
    (22, 'Fluid Mechanics', 'Frank M. White', 'A comprehensive textbook on fluid mechanics, covering both fundamentals and applications.', 2016, 8),
    (23, 'Materials Science and Engineering: An Introduction', 'William D. Callister Jr., David G. Rethwisch', 'An introductory text on materials science and engineering, covering materials properties, processing, and applications.', 2017, 10),
    (24, 'Principles of Environmental Engineering & Science', 'Mackenzie Davis, Susan Masten', 'An introduction to environmental engineering principles and their applications.', 2016, 3),
    (25, 'Control Systems Engineering', 'Norman S. Nise', 'A comprehensive textbook covering the analysis and design of control systems.', 2015, 7),
    (26, 'Mechanics of Materials', 'Russell C. Hibbeler', 'A textbook covering the mechanics of deformable bodies and the behavior of materials under loading.', 2018, 10),
    (27, 'Introduction to Thermodynamics and Heat Transfer', 'Yunus A. Çengel', 'An introductory textbook on thermodynamics and heat transfer, with engineering applications.', 2019, 2),
    (28, 'Engineering Economy', 'William G. Sullivan, Elin M. Wicks, C. Patrick Koelling', 'A textbook covering the principles and techniques of engineering economy analysis.', 2018, 17),
    (29, 'Electric Machinery Fundamentals', 'Stephen J. Chapman', 'An introductory textbook on electric machinery and transformers.', 2017, 5);


-- Inserting data values for book copies into the book_copy table
INSERT INTO `book_copy`(`info_id`,`book_id`,`is_available`) VALUES
(15, 16, 1),
(16, 17, 1),
(17, 18, 1),
(18, 19, 1),
(19, 20, 1),
(20, 21, 1),
(21, 22, 1),
(22, 23, 1),
(23, 24, 1),
(24, 25, 1),
(25, 26, 1),
(26, 27, 1),
(27, 28, 1),
(28, 29, 1),
(29, 30, 1),
(15, 31, 1),
(16, 32, 1),
(17, 33, 1),
(18, 34, 1),
(19, 35, 1),
(20, 36, 1),
(21, 37, 1),
(22, 38, 1),
(23, 39, 1),
(24, 40, 1);


-- Inserting data values for book categories into the book_category table
INSERT INTO `book_category`(`info_id`,`category`) VALUES
(15, 'Computer Science'),
(16, 'Mechanical Engineering'),
(17, 'Electrical Engineering'),
(18, 'Civil Engineering'),
(19, 'Computer Engineering'),
(20, 'Electrical Engineering'),
(21, 'Mechanical Engineering'),
(22, 'Mechanical Engineering'),
(23, 'Materials Science'),
(24, 'Environmental Engineering'),
(25, 'Control Systems Engineering'),
(26, 'Mechanical Engineering'),
(27, 'Thermodynamics'),
(28, 'Engineering Economics'),
(29, 'Electrical Engineering');
