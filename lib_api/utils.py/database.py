import mysql.connector as mysql


class DB:
    _connection:mysql.MySQLConnection = None;

    @staticmethod
    def get_connection():
        if DB._connection is None:
            DB._connection = mysql.connect(
                host='localhost',
                port='3306',
                user='root',
                passwd='password',
                database='lib',
            )
        return DB._connection
    

        
if __name__ == '__main__':

    cursor = DB.get_connection().cursor()
    print(cursor.execute("describe lib"))



    
    