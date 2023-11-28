class Book:
    X = 5

    def __init__(self) -> None:
        self.x = 100

    def display(self):
        return f"x: {self.x} - X.Book: {Book.X}"


b = Book()
print(b.display())

print("Cambiando el valor del atributo de la clase") 
Book.X = 6
print(b.display())

print(f"Atributo de instancia: {b.x} - Atributo de clase: {Book.X} ")

print(f"Atributo de clase (Book.X), llamado por la instancia (b.X): {b.X}")