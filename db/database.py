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
            user="postgres",
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
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            RETURNING user_id, firstname, lastname, othernames,
            username, email, phone_number, is_admin, created_on;
            """.format(firstname, lastname, othernames, username,
                       email, password, phone_number, created_on)
        )
        user = self.cursor.fetchone()
        return user

    def check_login_credentials(self, username, password):
        """
        checks for user login credentials
        """
        user_query = """
            SELECT username, password FROM users\
            WHERE username = '{}' AND password = '{}'""".format(username, password)
        self.cursor.execute(user_query)
        user = self.cursor.fetchone()
        return user

    def insert_incident_data(self, *args):
        """
        insert incidents data into table
        """
        incident_type = args[0]
        location = args[1]
        status = args[2]
        images = args[3]
        videos = args[4]
        comment = args[5]
        created_on = args[6]
        created_by = args[7]
        self.cursor.execute(
            """
            INSERT INTO incidents(incident_type, location, status, images,
                                  videos, comment, created_on, created_by)
            VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') RETURNING *;
            """.format(incident_type, location, status, images,
                       videos, comment, created_on, created_by)
        )
        incident = self.cursor.fetchone()
        return incident

    def update_incident(self, *args):
        """
        updates an incident
        """
        incident_type = args[0]
        location = args[1]
        status = args[2]
        images = args[3]
        videos = args[4]
        comment = args[5]
        incident_id = args[6]
        self.cursor.execute(
            """
            UPDATE incidents SET incident_type = '{}', location = '{}',
            status = '{}', images = '{}', videos = '{}', comment = '{}'
            WHERE incident_id = '{}'
            RETURNING *;
            """
            .format(incident_type, location, status, images, videos, comment, incident_id)
        )
        incident = self.cursor.fetchone()
        return incident

    def fetch_all(self, table):
        """
        returns all rows from a table
        """
        self.cursor.execute("""SELECT * FROM {};""".format(table))
        rows = self.cursor.fetchall()
        return rows

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

    def get_all_by_argument(self, table, column, argument):
        """
        returns a list of rows by argument
        """
        self.cursor.execute(
            """
            SELECT * FROM {} WHERE {} = '{}'
            """.format(table, column, argument)
        )
        result = self.cursor.fetchall()
        return result

    def delete_by_argument(self, table, column, argument):
        """
        deletes a rows by argument
        """
        self.cursor.execute(
            """
            DELETE FROM {} WHERE {} = '{}'
            """.format(table, column, argument))

    def drop_tables(self):
        """
        drop all tables
        """
        drop_query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users", "incidents"]
        for table in tables:
            self.cursor.execute(drop_query.format(table))
