class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        return f"Name: {self.name} - Age: {self.age}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be beetwen 20 and 80")
    

    


if __name__ == "__main__":
    p = Person("Robert", 20)

    print(p.display())
    p.age=65
    print(p.display())
    p.age=70
    print(p.display())
