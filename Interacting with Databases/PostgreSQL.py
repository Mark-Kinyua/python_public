import psycopg2


# Steps to connect:
# 1. Connect to the db
#     Pass the Dbname, User, Password and Port
# 2. Create cursor object
# 3. Write a SQL Query
# 4. Commit Changes
# 5. Close DB Connections

def create_table():
    connection = psycopg2.connect("dbname='test1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert_data(item, quantity, price):
    connection = psycopg2.connect("dbname='test1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect("dbname='test1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = psycopg2.connect("dbname='test1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    connection.commit()
    connection.close()


def update(quantity, price, item):
    connection = psycopg2.connect("dbname='test1' user='postgres' password='postgres' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()
    connection.close()


# create_table()

print(view())
# delete(input("Enter what to delete: "))

# insert_data(input("Enter the item: "),
#            input("Enter the quantity: "),
#            input("Enter the price: "))

update(input("Enter the quantity: "),
       input("Enter the price: "),
       input("Enter the item: "))

# print(view())
