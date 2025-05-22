#Library Manager
#Rashen Thao
#This code connects to SQLite and store the database for books.

import sqlite3

DB_NAME = "Final.sqlite"

def connect():
    return sqlite3.connect(DB_NAME)

def get_books():
    with connect() as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT,
                year INTEGER
            )
        ''')
        cur.execute("SELECT * FROM books ORDER BY year DESC")
        return cur.fetchall()

def add_book(book):
    with connect() as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO books (title, author, genre, year)
            VALUES (?, ?, ?, ?)
        ''', book)
        conn.commit()
        print(f"{book[0]} by {book[1]} was added.")

def search_books(field, value):
    with connect() as conn:
        cur = conn.cursor()
        query = f"SELECT * FROM books WHERE {field} LIKE ? ORDER BY year DESC"
        cur.execute(query, (f"%{value}%",))
        return cur.fetchall()
