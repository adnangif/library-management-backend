from typing import Any, Dict
from .database import *
# from database import *

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
