import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")





def main():
    connection = create_connection("zoo_magazin.sqlite")


    create_product_table = """
        CREATE TABLE IF NOT EXISTS product (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title VARCHAR(255) NOT NULL,
          price INTEGER NOT NULL,
          gender TEXT NOT NULL,
          type_product TEXT NOT NULL
        );
        """
    execute_query(connection, create_product_table)

if __name__ == "__main__":
    main()
