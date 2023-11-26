class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"I am {self.name}"

    def greet(self):
        if self.age < 80:
            return "Hello, how are you doing?"
        else:
            return "Hello, how do you do"
        self.display()

    def get_old(self):
         self.age = 75
         return self.age 

class Test:
    pass      

if "__main__" == __name__:
    p1 = Person("César", 90)
    p2 = Person("Vero", 43)

    # print(id(Person))
    # print(type(p1))
    # print(type(p2))
    # print(id(p1))
    # print(id(p2))
    # print(p1)
    # print(p2)

    # print(p1.name)
    # print(p1.age)
    # print(p2.name)
    # print(p2.age)

    # print(p1.display())
    # print(p1.greet())

    # print(p2.display())
    # print(p2.greet())

    # print(p1.get_old())

    t1 = Test()
    t2 = Test()

    print(t1 == t2, end = ' ')
    print(type(t1) == type(t2), end = ' ')