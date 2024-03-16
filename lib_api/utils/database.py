import mysql.connector as mysql
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from mysql_credentials import Credentials


class DB:
    _connection:MySQLConnectionAbstract|PooledMySQLConnection|None = None; 

    @staticmethod
    def get_connection():
        if DB._connection is None:
            DB._connection = mysql.connect(
                host=Credentials.host,
                port=Credentials.port,
                user=Credentials.user,
                passwd=Credentials.passwd,
                database=Credentials.database,
            )
        return DB._connection
    

        
if __name__ == '__main__':

    cursor = DB.get_connection().cursor()
    print(cursor.execute("describe lib"))



    
    