import os
import mysql.connector
from dotenv import load_dotenv

class DbService:

    def __init__(self):
        load_dotenv()
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_pass = os.getenv("DB_PASS")
        self.db_host = os.getenv("DB_HOST")

    def query(self, query, params=None):
        conn = None
        curs = None
        try:
            conn, curs = self.__create_connection()
            curs.execute(query, params)
            return curs.fetchall()
        finally:
            if curs:
                curs.close()
            if conn:
                conn.close()

    def command(self, command):
        conn = None
        curs = None
        try:
            conn, curs = self.__create_connection()
            curs.execute(command)
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if curs:
                curs.close()
            if conn:
                conn.close()

    def __create_connection(self):
        connection = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_pass,
            database=self.db_name
        )
        cursor = connection.cursor()
        return connection, cursor