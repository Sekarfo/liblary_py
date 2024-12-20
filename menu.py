import sqlite3
from bookstore import Bookstore
from person import Person


bookstore = Bookstore("bookstore.db")

person = Person("Имя покупателя", bookstore)


bookstore.cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author VARCHAR(255),
    year DATE,
    genre TEXT,
    price REAL,
    amount INTEGER
)
''')
bookstore.conn.commit()


def main_menu():
    while True:
        print("\nДобро пожаловать в библиотеку!")
        print("Выберите действие:")
        print("1. Добавить книгу ")
        print("2. Удалить книгу ")
        print("3. Обновить данные книги")
        print("4. Найти книгу")
        print("5. Купить книгу")
        print("6. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            add_book_menu()
        elif choice == "2":
            delete_book_menu()
        elif choice == "3":
            update_book_menu()
        elif choice == "4":
            search_books_menu()
        elif choice == "5":
            buy_book_menu()
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите корректный номер.")


def add_book_menu():
    print("\nДобавление книги")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска (YYYY-MM-DD): ")
    genre = input("Введите жанр книги: ")
    price = float(input("Введите цену книги: "))
    amount = int(input("Введите количество экземпляров: "))
    
    bookstore.add_book(title, author, year, genre, price, amount)
    print(f"Книга '{title}' успешно добавлена!")


def delete_book_menu():
    print("\nУдаление книги")
    book_title = input("Введите название книги для удаления: ")
    bookstore.delete_book(book_title)
    print(f"Книга '{book_title}' успешно удалена!")


def update_book_menu():
    print("\nОбновление данных книги")
    
    title = input("Введите название книги, которую хотите обновить: ")

    print("Введите новые значения для книги (оставьте пустым, чтобы не изменять поле):")
    author = input("Автор: ") or None
    year = input("Год выпуска (YYYY-MM-DD): ") or None
    genre = input("Жанр: ") or None
    price = input("Цена: ") or None
    amount = input("Количество: ") or None

    price = float(price) if price else None
    amount = int(amount) if amount else None

    bookstore.update_book(
        title=title,
        author=author,
        year=year,
        genre=genre,
        price=price,
        amount=amount
    )
    print(f"Данные книги '{title}' успешно обновлены!")


def search_books_menu():
    print("\nПоиск книги по названию")

    title = input("Введите название книги: ").strip()

    if not title:
        print("Ошибка: Название книги не может быть пустым.")
        return

    
    result = bookstore.search_book(title=title)

    if result:
        print("\nНайденная книга:")
        print(f"Название: {result['title']}, Автор: {result['author']}, Год выпуска: {result['year']}, "
              f"Жанр: {result['genre']}, Цена: {result['price']}, Количество: {result['amount']}")
    else:
        print("Книга с таким названием не найдена.")


def buy_book_menu():
    print("\nПокупка книги")
    
    title = input("Введите название книги для покупки: ").strip()
    
    if not title:
        print("Ошибка: Название книги не может быть пустым.")
        return

    
    if person.buy_book(title):
        print(f"Вы успешно купили книгу '{title}'.")
    else:
        print(f"Не удалось купить книгу '{title}'.")


if __name__ == "__main__":
    try:
        main_menu()
    finally:
        bookstore.close_connection()
