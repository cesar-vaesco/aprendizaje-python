class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publiser = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError("Price cannot be less than 10 or more than 500")

    def display(self):
        return f"""
ISBN: {self.isbn}
Author: {self.author}
Publisher: {self.publiser}
Pages: {self.pages}
Price: {self.price}
Copies: {self.copies}
"""

    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False

    def shell(self):
        if self.in_stock() == True:
            self.copies -= 1
            return f"Book: {self.title} - Copies: {self.copies}"
        else:
            return "the book is out of stock"


"""
Cree otro método llamado vender que disminuya el número de copias en 1 si el libro está en stock; 
de lo contrario, imprimirá el mensaje de que el libro está agotado.

"""

book1 = Book("957-4-36-547417-1", "Learn Physics", "Stephen", "CBC", 350, 200, 10)
book2 = Book("652-6-86-748413-3", "Learn Chemistry", "Jack", "CBC", 400, 220, 20)
book3 = Book("957-7-39-347216-2", "Learn Maths", "John", "XYZ", 500, 300, 5)
book4 = Book("957-7-39-347216-3", "Learn Biology", "Jack", "XYZ", 400, 200, 6)
book5 = Book("957-7-39-347216-4", "Sex Education", "Cheshare", "FGH", 400, 500, 0)

print("Stock".center(100, "*"))
print(f"Stock book1: {book1.in_stock()}")
print(f"Stock book5: {book5.in_stock()}")


print("Decreases copies in stock".center(100, "*"))
print(book1.shell())


books = [book1, book2, book3, book4, book5]

print(" Print list the books ".center(100, "-"))
for book in books:
    print(book.display())

jack_books = [book.title for book in books if book.author == "Jack"]

print(" Search books written for Jack".center(100, "-"))
print(jack_books)
