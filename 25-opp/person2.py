class Person:
    species = "Homo Sapiens"
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        return (
            f"{self.name} is {self.age} years old and is the species {Person.species}"
        )

    @classmethod
    def show_count(cls):
        return f"There are {cls.count} {cls.species}"


print(Person.show_count())

p1 = Person("Vane", 15)
p2 = Person("Magali", 41)

print(p1.display())
print(p2.display())

print(Person.show_count())
print(f"Class person instances: {Person.count}")

p3 = Person("Charly", 15)
p4 = Person("Britany", 41)

print(f"Class person instances: {Person.count}")

print(Person.show_count())
