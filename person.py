from bookstore import Bookstore

class Person:
    def __init__(self, name, bookstore):
        self.name = name
        self.bookstore = bookstore

    def search_book(self, title):
        return self.bookstore.search_book(title)

    def buy_book(self, title):
        
        book = self.bookstore.search_book(title)

        if book and book['amount'] > 0:  
            self.bookstore.update_book(
                title=title,
                author=book['author'],  
                year=book['year'],
                genre=book['genre'],
                price=book['price'],
                amount=book['amount'] - 1  
            )
            print(f"Книга '{title}' успешно куплена!")
            return True
        else:
            print(f"Книга '{title}' не найдена или закончилась на складе.")
            return False
