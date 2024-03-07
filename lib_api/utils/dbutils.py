from .database import *
# from database import *

def createUser(parsed: dict) -> bool:

    try:
        iid=parsed['iid']
        fname=parsed['fname']
        lname=parsed['lname']
        email=parsed['email']
        phone=parsed['phone']
        password=parsed['password']
        maintainer=parsed['maintainer']

        cursor = DB.get_connection().cursor()
        cursor.execute('''
                        INSERT INTO user(institution_id_number,first_name,last_name,hashed_pass,email,phone,is_maintainer)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        ''',[iid,fname,lname,password,email,phone,maintainer])
        DB.get_connection().commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


if __name__ == "__main__":
    print(signup(
        234234,'asdfasd','asdf43','q4rcsdcfsfd','234234','era3q4dsafsd'
    ))
