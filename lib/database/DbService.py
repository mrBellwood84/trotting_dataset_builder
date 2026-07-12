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

    def query(self, query, params = None):
        conn, curs = self.__create_connection()
        curs.execute(query, params)
        return curs.fetchall()


    def __create_connection(self):

        connection = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_pass,
            database=self.db_name
        )

        cursor = connection.cursor()
        return connection, cursor