from typing import Any, Dict
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
        iid=parsed['iid']
        fname=parsed['fname']
        lname=parsed['lname']
        email=parsed['email']
        phone=parsed['phone']
        password=parsed['password']

        hashed_pass = hasher.encode(password=password,salt=secrets.token_hex())

        cursor.execute('''
                        INSERT INTO user(institution_id_number,first_name,last_name,hashed_pass,email,phone)
                        values(%s,%s,%s,%s,%s,%s)
                        ''',[iid,fname,lname,hashed_pass,email,phone])
        DB.get_connection().commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def find_book_by_str(q:str|None = None):
    if q is None:
        q = ""
        
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        query = "%" + q + "%"
        
        args = [query,query,query,query,query]
        cursor.execute( '''
        SELECT * 
        FROM book_info
        WHERE 
            LOWER(title) LIKE LOWER(%s) OR
            LOWER(author) LIKE LOWER(%s) OR
            LOWER(description) LIKE LOWER(%s) OR
            LOWER(publication_year) LIKE LOWER(%s) OR
            LOWER(edition) LIKE LOWER(%s) 
                        ''',args)
        
        result:Dict|Any = cursor.fetchall()
        cursor.close()
        
        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None
    
    
def get_category_list():
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        cursor.execute( '''
        SELECT DISTINCT category
        FROM book_category
                        ''')
        
        result:Dict|Any = cursor.fetchall()
        cursor.close()
        
        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None
    
    
def get_category_books(q:str|None = None):
    if q is None:
        q = ""
        
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        args = [q]
        cursor.execute( '''
        SELECT * 
        FROM book_category NATURAL JOIN book_info
        WHERE LOWER(book_category.category) = LOWER(%s)
                        ''', args)
        
        result:Dict|Any = cursor.fetchall()
        cursor.close()
        
        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None
    
def get_available_books_using_info_id(q:str|None = None):
    if q is None:
        q = ""
        
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        args = [q]
        cursor.execute( '''
        SELECT * 
        FROM book_copy NATURAL JOIN book_info
        where 
            book_info.info_id = %s AND
            book_copy.is_available = 1
                        ''', args)
        
        result:Dict|Any = cursor.fetchall()
        cursor.close()
        
        return result

    except Exception as e:
        print(e)
        cursor.close()
        return None
    

def create_order_using_user_id(user_id):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        DUE_TIME = 180
        LAST_COLLECTION_TIME = 5
        cursor.execute('''
        INSERT INTO `order` (`order_id`, `user_id`, `issue_datetime`, `due_datetime`, `last_collection_time`) 
        VALUES (NULL, %s, current_timestamp(), %s, %s);
        ''',[user_id,DUE_TIME,LAST_COLLECTION_TIME])
        DB.get_connection().commit()
        
        cursor.execute('SELECT LAST_INSERT_ID()')
        
        order_id:dict|Any = cursor.fetchone()
        
        order_id = order_id.get('LAST_INSERT_ID()')
        
        return {
            "order_id":order_id
        }

    except Exception as e:
        print(e)
        cursor.close()
        return None
    
    
def add_book_to_order(parsed):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        order_id = parsed.get('order_id')
        book_id = parsed.get('book_id')
        
        cursor.execute(''' 
        INSERT INTO ordered_book (order_id,book_id)
        VALUES (%s,%s)
        ''',[order_id,book_id])
        
        cursor.execute('''
        UPDATE book_copy
        SET is_available = 0
        WHERE book_id = %s
        ''',[book_id])
        
        DB.get_connection().commit()
        return {
            "message":"successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message":"failure"
        }
        
        
        
def delete_order(parsed):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        order_id = parsed.get('order_id')
        
        cursor.execute(''' 
        SELECT book_id 
        FROM ordered_book 
        WHERE order_id = %s
        ''',[order_id])
        
        book_list = cursor.fetchall()
        
        for book in book_list:
            book:dict|Any = book
            
            book_id = book.get('book_id')
            
            cursor.execute('''
            UPDATE book_copy
            SET is_available = 1
            WHERE book_id = %s
            ''',[book_id])
            
            cursor.execute('''
            DELETE FROM ordered_book
            WHERE book_id = %s
            ''',[book_id])
        DB.get_connection().commit()
        
        cursor.execute('''
        DELETE FROM `order`
        WHERE `order`.`order_id` = %s
        ''',[order_id])
        
        DB.get_connection().commit()
        return {
            "message":"successful"
        }

    except Exception as e:
        print(e)
        cursor.close()
        return {
            "message":"failure"
        }
        
        


def get_orders(user_id:str):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        
        cursor.execute('''
        SELECT * 
        FROM `order`
        WHERE `user_id` = %s
        ''',[user_id])       

        orders = cursor.fetchall()
        
        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_order_details(order_id:str, user_id:str):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        
        cursor.execute('''
        SELECT * 
        FROM `order`
        WHERE 
            `order_id` = %s AND
            `user_id` = %s

        ''',[order_id, user_id])       

        orders = cursor.fetchone()
        
        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None

def get_book_details(book_id:str):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        
        cursor.execute('''
        SELECT * 
        FROM `book_info` NATURAL JOIN `book_copy`
        WHERE 
            `book_id` = %s

        ''',[book_id])       

        orders = cursor.fetchone()
        
        return orders

    except Exception as e:
        print(e)
        cursor.close()
        return None


def get_related_books(order_id:str):
    
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        
        cursor.execute('''
            SELECT *
            FROM (`ordered_book` NATURAL JOIN `book_copy`) NATURAL JOIN `book_info`
            WHERE `order_id` = %s

        ''',[order_id])       

        books = cursor.fetchall()
        
        return books

    except Exception as e:
        print(e)
        cursor.close()
        return None

def find_by_iid_and_password(parsed: dict):
    cursor = DB.get_connection().cursor(dictionary=True)
    try:
        iid=parsed['iid']
        password=parsed['password']
        cursor.execute( '''
        SELECT user_id, hashed_pass, institution_id_number, first_name, last_name, email 
        FROM user
        WHERE institution_id_number=%s 
                        ''',[iid])
        
        tried_user:Dict|Any = cursor.fetchone()
        cursor.close()


        if(tried_user == None):
            return None

        pass_compare_result = hasher.verify(password=password,encoded=tried_user['hashed_pass'])
        tried_user.pop('hashed_pass')

        if(pass_compare_result == True):
            return tried_user 
        
        return None
        

    except Exception as e:
        print(e)
        cursor.close()
        return None


if __name__ == "__main__":
    print(
        find_by_iid_and_password({
            'iid':210210,
            'password':'sdfasdfasd'
        })
    )
    # print(createUser(
    #     234234,'asdfasd','asdf43','q4rcsdcfsfd','234234','era3q4dsafsd'
    # ))
