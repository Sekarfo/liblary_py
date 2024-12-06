from bookstore import Bookstore
class Person:
    def __init__(self, name, bookstore):
        self.name = name
        self.bookstore = bookstore

    def search_book(self, **criteria):
        self.bookstore.search_book(**criteria)

    def buy_book(self, title):
    
        book = Bookstore(bookstore.db)
        book = self.bookstore.get_book_by_title(title)
    
    
        if book and book['amount'] > 0: 
            self.bookstore.update_book(
                title=title,
                author=book['author'],  
                year=book['year'],
                genre=book['genre'],
                price=book['price'],
                amount=book['amount'] - 1          )
            return True
        else:
            return False
