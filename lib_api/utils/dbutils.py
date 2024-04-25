from typing import Any, Dict

import django.db
import mysql.connector

from .database import *

from django.contrib.auth.hashers import PBKDF2PasswordHasher
import secrets

hasher = PBKDF2PasswordHasher()


def find_user_using_token(parsed: dict):
    print(parsed)
    pass


def createUser(parsed: dict) -> bool:
    cursor = DB.get_connection().cursor()
    try:
        iid = parsed['iid']
        fname = parsed['fname']
        lname = parsed['lname']
        email = parsed['email']
        phone = parsed['phone']
        password = parsed['password']

        hashed_pass = hasher.encode(password=password, salt=secrets.token_hex())

        cursor.execute('''
                        INSERT INTO user(institution_id_number,first_name,last_name,hashed_pass,email,phone)
                        values(%s,%s,%s,%s,%s,%s)
                        ''', [iid, fname, lname, hashed_pass, email, phone])
        DB.get_connection().commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def find_book_by_str(q: str | None = None):
    if q is None:
        q = ""

    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        query = "%" + q + "%"

        args = [query, query, query, query, query]
        cursor.execute('''
        SELECT * 
        FROM book_info
        WHERE 
            LOWER(title) LIKE LOWER(%s) OR
            LOWER(author) LIKE LOWER(%s) OR
            LOWER(description) LIKE LOWER(%s) OR
            LOWER(publication_year) LIKE LOWER(%s) OR
            LOWER(edition) LIKE LOWER(%s) 
                        ''', args)

        result: Dict | Any = cursor.fetchall()
        cursor.close()

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_category_list():
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        cursor.execute('''
        SELECT DISTINCT category
        FROM book_category
                        ''')

        result: Dict | Any = cursor.fetchall()
        cursor.close()

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_category_books(q: str | None = None):
    if q is None:
        q = ""

    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        args = [q]
        cursor.execute('''
        SELECT `info_id` ,`category`,`title`,`author`,`description`,`publication_year`,`edition`
        FROM (book_category NATURAL JOIN book_info) NATURAL JOIN `book_copy`
        WHERE 
            LOWER(book_category.category) = LOWER(%s)
        GROUP BY `info_id` ,`category`,`title`,`author`,`description`,`publication_year`,`edition`

                        ''', args)

        result: Dict | Any = cursor.fetchall()
        cursor.close()

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_available_books_using_info_id(q: str | None = None):
    if q is None:
        q = ""

    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        args = [q]
        cursor.execute('''
        SELECT * 
        FROM book_copy NATURAL JOIN book_info
        where 
            book_info.info_id = %s AND
            book_copy.is_available = 1
        LIMIT 1
                        ''', args)

        result: Dict | Any = cursor.fetchone()
        cursor.close()

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def create_order_using_user_id(user_id, parsed):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        book_ids: list[str] = parsed["book_ids"]
        DUE_TIME = 180
        LAST_COLLECTION_TIME = 5
        cursor.execute('''
        INSERT INTO `order` (`order_id`, `user_id`, `issue_datetime`, `due_datetime`, `last_collection_time`) 
        VALUES (NULL, %s, current_timestamp(), %s, %s);
        ''', [user_id, DUE_TIME, LAST_COLLECTION_TIME])
        DB.get_connection().commit()

        cursor.execute('SELECT LAST_INSERT_ID()')

        order_id: dict | Any = cursor.fetchone()

        order_id = str(order_id.get('LAST_INSERT_ID()'))

        for book_id in book_ids:
            cursor.execute('''
            SELECT * 
            FROM `book_copy` 
            WHERE   `book_id` = %s AND
                    `is_available` = 1
            ''', [book_id])

            if (len(cursor.fetchall()) == 0):
                cursor.execute('''DELETE FROM `order` WHERE `order_id` = %s''', [order_id])
                DB.get_connection().commit()

                raise Exception("Not enough available books")

            cursor.execute('''  
                INSERT INTO `ordered_book` (`order_id`, `book_id`) 
                SELECT %s AS `order_id`, `book_id` 
                FROM `book_copy`
                WHERE 
                    `is_available` = 1 AND
                    `book_id` = %s
                ''', [order_id, book_id])

            cursor.execute('''
                UPDATE `book_copy`
                SET `is_available` = 0
                WHERE `book_id` = %s
            ''', [book_id])

        DB.get_connection().commit()
        return {
            "message": "successful",
            "order_id": order_id,
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message": str(e)
        }


def add_book_to_order(parsed):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        order_id = parsed.get('order_id')
        book_id = parsed.get('book_id')

        cursor.execute(''' 
        INSERT INTO ordered_book (order_id,book_id)
        VALUES (%s,%s)
        ''', [order_id, book_id])

        cursor.execute('''
        UPDATE book_copy
        SET is_available = 0
        WHERE book_id = %s
        ''', [book_id])

        DB.get_connection().commit()
        return {
            "message": "successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message": "failure"
        }


def delete_order(parsed):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        order_id = parsed.get('order_id')

        cursor.execute(''' 
        SELECT book_id 
        FROM ordered_book 
        WHERE order_id = %s
        ''', [order_id])

        book_list = cursor.fetchall()

        for book in book_list:
            book: dict | Any = book

            book_id = book.get('book_id')

            cursor.execute('''
            UPDATE book_copy
            SET is_available = 1
            WHERE book_id = %s
            ''', [book_id])

            cursor.execute('''
            DELETE FROM ordered_book
            WHERE book_id = %s
            ''', [book_id])
        DB.get_connection().commit()

        cursor.execute('''
        DELETE FROM `order`
        WHERE `order`.`order_id` = %s
        ''', [order_id])

        DB.get_connection().commit()
        return {
            "message": "successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message": "failure"
        }


def get_orders(user_id: str):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:

        cursor.execute('''
        SELECT * 
        FROM `order`
        WHERE `user_id` = %s
        ''', [user_id])

        orders = cursor.fetchall()

        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_order_details(order_id: str, user_id: str):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:

        cursor.execute('''
        SELECT * 
        FROM `order`
        WHERE 
            `order_id` = %s AND
            `user_id` = %s
        LIMIT 1
        ''', [order_id, user_id])

        orders = cursor.fetchone()

        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_book_details(info_id: str):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:

        cursor.execute('''
        SELECT *
        FROM `book_info` NATURAL JOIN `book_copy`
        WHERE `info_id` = %s
        ORDER BY `is_available` DESC
        LIMIT 1
        ''', [info_id])

        orders = cursor.fetchone()

        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_related_books(order_id: str):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:

        cursor.execute('''
            SELECT *
            FROM (`ordered_book` NATURAL JOIN `book_copy`) NATURAL JOIN `book_info`
            WHERE `order_id` = %s

        ''', [order_id])

        books = cursor.fetchall()

        return books

    except Exception as e:
        print(e)
        cursor.close()
        return None


def find_by_iid_and_password(parsed: dict):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        iid = parsed['iid']
        password = parsed['password']
        cursor.execute('''
        SELECT user_id, hashed_pass, institution_id_number, first_name, last_name, email 
        FROM user
        WHERE institution_id_number=%s 
                        ''', [iid])

        tried_user: Dict | Any = cursor.fetchone()
        cursor.close()

        if (tried_user == None):
            return None

        pass_compare_result = hasher.verify(password=password, encoded=tried_user['hashed_pass'])
        tried_user.pop('hashed_pass')

        if (pass_compare_result == True):
            return tried_user

        return None


    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_all_ordered_books():
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        cursor.execute('''
        SELECT *
        FROM (`book_info` NATURAL JOIN `book_copy`) NATURAL JOIN `ordered_book`
                        ''')

        result = cursor.fetchall()

        cursor.close()

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def validate_librarian_iid_password(parsed: dict):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        iid = parsed['iid']
        password = parsed['password']
        cursor.execute('''
        SELECT *
        FROM `librarian`
        WHERE institution_id_number=%s 
                        ''', [iid])

        tried_user: Dict | Any = cursor.fetchone()
        cursor.close()

        if (tried_user == None):
            return None

        pass_compare_result = hasher.verify(password=password, encoded=tried_user['hashed_pass'])
        tried_user.pop('hashed_pass')

        if (pass_compare_result == True):
            return tried_user

        return None


    except Exception as e:
        print(e)
        cursor.close()
        return None


def create_librarian(parsed: dict) -> bool:
    cursor = DB.get_connection().cursor()
    try:
        iid = parsed['iid']
        fname = parsed['fname']
        lname = parsed['lname']
        email = parsed['email']
        phone = parsed['phone']
        password = parsed['password']

        hashed_pass = hasher.encode(password=password, salt=secrets.token_hex())

        cursor.execute('''
                        INSERT INTO librarian(institution_id_number,first_name,last_name,hashed_pass,email,phone)
                        values(%s,%s,%s,%s,%s,%s)
                        ''', [iid, fname, lname, hashed_pass, email, phone])
        DB.get_connection().commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def librarian_deliver_book_handle_db(parsed, librarian_id):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        book_id = parsed.get('book_id')

        cursor.execute(''' 
            SELECT *
            FROM `ordered_book` WHERE `book_id`=%s;
        ''', [book_id])

        book = cursor.fetchone()

        order_id = book['order_id']

        cursor.execute('''
            INSERT INTO `borrow_record`(`collection_date`,`delivered_by`,`order_id`)
            VALUES(CURRENT_DATE(),%s,%s)
        
        ''', [librarian_id, order_id])

        DB.get_connection().commit()

        cursor.execute('''SELECT LAST_INSERT_ID()''')
        result = cursor.fetchone()
        borrow_id = result['LAST_INSERT_ID()']

        cursor.execute('''
            INSERT INTO `borrowed_book`(book_id, borrow_id) 
            VALUES (%s,%s)
        ''', [book_id, borrow_id])

        cursor.execute('''
            DELETE FROM `ordered_book`
            WHERE order_id=%s
        ''', [order_id])

        DB.get_connection().commit()
        cursor.close()

        return {
            "message": "successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message": "failure"
        }


def get_all_borrowed_books():
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        cursor.execute('''
        SELECT `book_id`,`book_info`.*
        FROM (`borrowed_book` NATURAL JOIN `book_copy`) NATURAL JOIN book_info
        ''')

        result = cursor.fetchall()

        cursor.close()

        print(result)

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None


def librarian_receive_book_handle_db(parsed, librarian_id):
    cursor = DB.get_connection().cursor(dictionary=True,buffered=True)

    try:
        book_id = parsed.get('book_id')

        cursor.execute(f''' 
            SELECT borrow_id,order_id
            FROM `borrowed_book` NATURAL JOIN `borrow_record`
            WHERE `book_id`=%s;
        ''', [book_id])

        book = cursor.fetchone()


        borrow_id = book["borrow_id"]
        order_id = book["order_id"]

        print(book)




        cursor.execute(f'''
            INSERT INTO `return_record`(book_return_date, order_id, return_to)
            VALUES(CURRENT_DATE(),%s,%s)

        ''',[order_id,librarian_id])


        DB.get_connection().commit()

        cursor.execute('''SELECT LAST_INSERT_ID()''')
        result = cursor.fetchone()
        return_id = result['LAST_INSERT_ID()']

        cursor.execute('''
            INSERT INTO `returned_book`(book_id, return_id) 
            VALUES (%s,%s);

       
        ''', [book_id, return_id])

        cursor.execute('''
        DELETE FROM `borrowed_book`
        where borrow_id=%s;
        ''',[borrow_id])

        cursor.execute('''
        UPDATE `book_copy`
        SET `is_available` = 1
        WHERE `book_id`=%s;
        
        ''',[book_id])

        cursor.close()
        DB.get_connection().commit()


        return {
            "message": "successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message": "failure"
        }



def get_user_borrowed_books(user_id:str):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        cursor.execute('''
        SELECT `book_copy`.book_id, `book_info`.*
        FROM (((`borrowed_book` NATURAL JOIN `borrow_record`) NATURAL JOIN `order`) NATURAL JOIN `book_copy`) NATURAL JOIN `book_info`
        WHERE `user_id` = %s
        ''',[user_id])

        result = cursor.fetchall()

        cursor.close()

        print(result)

        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None