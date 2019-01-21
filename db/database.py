import os
from pprint import pprint
import psycopg2
from psycopg2.extras import RealDictCursor


class DbConnection:
    """
    This class represents the database connection
    """

    def __init__(self):
        """
        initialize database connection
        """
        if os.getenv('DB_NAME') == 'test_ireporter':
            self.db_name = 'test_ireporter'
        else:
            self.db_name = 'ireporter'
        pprint(self.db_name)
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user="murungi",
            password="myPassword",
            port="5432"
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        pprint("Successfully connected to the database.")

    def create_tables(self):
        """
        creates all database tables
        """
        with open('db/schema.sql') as tables:
            self.cursor.execute(tables.read())

    def insert_user_data(self, firstname, lastname, othernames, username, email, password, phone_number):
        """
        insert user data into the database
        """
        # firstname = args[1]
        # lastname = args[2]
        # othernames = args[3]
        # username = args[4]
        # email = args[5]
        # password = args[6]
        # phone_number = args[7]
        
        self.cursor.execute(
            """
            INSERT INTO users (firstname, lastname, othernames, username, email, password, phone_number)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')
            """.format(firstname, lastname, othernames, username, email, password, phone_number)
        )
        # user_id = self.cursor.fetchone()[0]

    def drop_tables(self):
        """
        drop all tables
        """
        drop_query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.execute(drop_query.format(table))
