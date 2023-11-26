class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        # diagonal declarado en el método init nunca cambiara sus valores iniciales
        # self.diagonal = (self.length * self.length + self.breadth * self.breadth)**0.5

    # Como propiedad, es posible cambiar los valores iniciales
    @property
    def diagonal(self):
        return (self.length * self.length + self.breadth * self.breadth)**0.5

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        return 2 * (self.length + self.breadth)
    
    def display(self):
        return f"""
Diagonal: {self.diagonal}
Area: {self.area()}
Parameter: {self.parameter()}

"""



r = Rectangle(2,5)

print(r.diagonal)
print(r.area())
print(r.parameter())
print(r.display())

r.length = 2
r.breadth = 4

print(r.display())
