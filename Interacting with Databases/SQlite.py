import sqlite3


# Steps to connect:
# 1. Connect to the db
# 2. Create cursor object
# 3. Write a SQL Query
# 4. Commit Changes
# 5. Close DB Connections

def create_table():
    connection = sqlite3.connect("lite.db")  # It automatically creates a db
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert_data(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()


def update(quantity, price, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    connection.commit()
    connection.close()

