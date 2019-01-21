"""
database class
"""

import os
from pprint import pprint
import psycopg2
from psycopg2.extras import RealDictCursor


class DatabaseConnection:
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
            user="jenny",
            password="myPassword",
            host="localhost",
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

    def insert_user_data(self, *args):
        """
        insert user data into the database
        """
        firstname = args[0]
        lastname = args[1]
        othernames = args[2]
        username = args[3]
        email = args[4]
        password = args[5]
        phone_number = args[6]
        created_on = args[7]
        self.cursor.execute(
            """
            INSERT INTO users(firstname, lastname, othernames,
                              username, email, password, phone_number, created_on)
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') RETURNING *;
            """.format(firstname, lastname, othernames, username,
                       email, password, phone_number, created_on)
        )
        user = self.cursor.fetchone()
        return user

    def get_by_argument(self, table, column, argument):
        """
        returns data by argument
        """
        self.cursor.execute(
            """
            SELECT * FROM {} WHERE {} = '{}'
            """.format(table, column, argument)
        )
        result = self.cursor.fetchone()
        return result

    def drop_tables(self):
        """
        drop all tables
        """
        drop_query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.execute(drop_query.format(table))
