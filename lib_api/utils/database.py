import mysql.connector as mysql
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
import json





class DB:
    _connection:MySQLConnectionAbstract|PooledMySQLConnection|None = None
    _credential:None|dict[str,str] = None

    @staticmethod
    def get_connection():
        if(DB._credential is None):
            with open('mysql_credentials.json') as fr:
                DB._credential = json.loads(fr.read())

        if DB._connection is None:
            DB._connection = mysql.connect(
                host=DB._credential['host'],
                port=DB._credential['port'],
                user=DB._credential['user'],
                passwd=DB._credential['passwd'],
                database=DB._credential['database'],
            )
        return DB._connection
    

        
if __name__ == '__main__':

    cursor = DB.get_connection().cursor()
    print(cursor.execute("describe lib"))



    
    