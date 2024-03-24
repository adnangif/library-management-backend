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

