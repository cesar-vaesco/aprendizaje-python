from employee_funtions import Employee
from datetime import datetime


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        return f"I am {self.name}, {self.age} years old"

    @classmethod
    def from_str(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["age"])

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name + " " + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name, age)


p1 = Person("Jhon", 20)
p2 = Person("Beth", 35)

s = "Jim, 23"
p3 = Person.from_str(s)

print(p3.display())

d = {"name": "Jane", "age": 34}
p4 = Person.from_dict(d)

print(p4.display())

e1 = Employee("James", "Smith", 1990, 6000)

print(e1.show())

p5 = Person.from_employee(e1)

print(p5.display())

print(datetime.now())
print(datetime.today())

x = datetime.now()
print(x.day)
print(f"Hora actual: {x.hour}:{x.minute}:{x.second:.0f}")