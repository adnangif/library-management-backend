import mysql.connector as mysql
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


class DB:
    _connection:MySQLConnectionAbstract|PooledMySQLConnection|None = None; 

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



    
    