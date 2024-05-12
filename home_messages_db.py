
import sqlite3

class HomeMessagesDB:
    def __init__(self, db_name):
        # Initialize the database connection
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        # Create a new table in the database
        column_definitions = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        # Insert data into the specified table
        placeholders = ', '.join(['?'] * len(data))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(insert_query, data)
        self.conn.commit()

    def remove_duplicates(self, table_name):
        # Remove duplicate rows from the specified table
        remove_duplicates_query = f"DELETE FROM {table_name} WHERE rowid NOT IN (SELECT MIN(rowid) FROM {table_name} GROUP BY <common_column>)"
        self.cursor.execute(remove_duplicates_query)
        self.conn.commit()

    def perform_join(self, table1, table2, common_column):
        # Perform a join operation between two tables
        join_query = f"SELECT * FROM {table1} LEFT JOIN {table2} ON {table1}.{common_column} = {table2}.{common_column}"
        self.cursor.execute(join_query)
        result = self.cursor.fetchall()
        return result

    def custom_query(self, query):
        # Execute a custom SQL query
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        # Close the database connection
        self.conn.close()
 


