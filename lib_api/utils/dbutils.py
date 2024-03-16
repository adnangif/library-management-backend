from .database import *
# from database import *

def createUser(parsed: dict) -> bool:
    cursor = DB.get_connection().cursor()
    try:
        iid=parsed['iid']
        fname=parsed['fname']
        lname=parsed['lname']
        email=parsed['email']
        phone=parsed['phone']
        password=parsed['password']

        cursor.execute('''
                        INSERT INTO user(institution_id_number,first_name,last_name,hashed_pass,email,phone)
                        values(%s,%s,%s,%s,%s,%s)
                        ''',[iid,fname,lname,password,email,phone])
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
        SELECT user_id, institution_id_number, first_name, last_name, email 
        FROM user
        WHERE institution_id_number=%s 
        AND hashed_pass=%s 
                        ''',[iid,password])
        
        rows = cursor.fetchall()
        cursor.close()

        if(len(rows) == 0):
            return None
        else:
            return rows[0]

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
