'''
# This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.

import sqlite3
import pandas as pd

class DatabaseProcessor:

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        """


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        """


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        """
'''

import sqlite3
import pandas as pd


class DatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)"
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        for item in data:
            insert_query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
            cursor.execute(insert_query, (item['name'], item['age']))

        conn.commit()
        conn.close()

    def search_database(self, table_name, name):

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        select_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()

        if result:
            return result
        else:
            return None

    def delete_from_database(self, table_name, name):

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()
