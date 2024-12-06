import sqlite3

class Bookstore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def add_book(self, title, author, year, genre, price, amount):
        self.cursor.execute('INSERT INTO books (title, author, year, genre, price, amount) VALUES (?, ?, ?, ?, ?, ?)',
                            (title, author, year, genre, price, amount))
        self.conn.commit()

    def delete_book(self, title):
        self.cursor.execute('DELETE FROM books WHERE title = ?', (title,))
        self.conn.commit()

    def update_book(self, title, author, year, genre, price, amount):
        self.cursor.execute('UPDATE books SET author = ?, year = ?, genre = ?, price = ?, amount = ? WHERE title = ?',
                            (author, year, genre, price, amount, title))
        self.conn.commit()

    def search_book(self, title):
        self.cursor.execute('SELECT title, author, year, genre, price, amount FROM books WHERE title = ?', (title,))
        row = self.cursor.fetchone()
        if row:
            return {
                'title': row[0],
                'author': row[1],
                'year': row[2],
                'genre': row[3],
                'price': row[4],
                'amount': row[5],
            }
        return None

    def close_connection(self):
        self.conn.close()
