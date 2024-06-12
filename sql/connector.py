from sys import exec_prefix
from ..logger import Logger
from ..configloader import Configuration as cfg
import mysql.connector
Log = Logger("mysql.main")

class ConnectionDetails:
    def __init__(self):
        creds = cfg().getCFG("sql")
        self.host = creds["host"]
        self.username = creds["username"]
        self.password = creds["password"]
        self.database = creds["database"]
        
class TestConnection(ConnectionDetails):
    def __init__(self):
        super().__init__()
        try:
            connection = mysql.connector.connect(
                host = self.host,
                user = self.username,
                password = self.password,
                database = self.database
            )
            if connection.is_connected():
                Log.info(f"Sikeres MYSQL csatlakozás! ({connection.database})")
                connection.close()
                
        except Exception as e:
            Log.error(e)


class MYSQL(ConnectionDetails):
    def __init__(self):
        super().__init__()
        
    def createConnection(self):
        try:
            connection = mysql.connector.connect(
                    host = self.host,
                    user = self.username,
                    password = self.password,
                    database = self.database
                )
            return connection  
        except Exception as e:
            Log.error(e)
            
    def read(self, query, parms=None):
        connection = self.createConnection()
        cursor = connection.cursor()
        try:
            if parms is not None:
                cursor.execute(query, parms)
            elif parms is None:
                cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            connection.close()
            return result
        except Exception as e:
            return False
    
    def write(self, query, parms):
        connection = self.createConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, parms)
            connection.commit()
            connection.close
            return True
        except Exception as e:
            Log.error(e)
            return False