import sqlite3


connection = sqlite3.connect('LocalBotDatabase.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    ''')

    connection.commit()



    


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()