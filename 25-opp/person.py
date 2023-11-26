class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError("Age must be beetwen 20 and 80")

    def display(self):
        return f"Name: {self.name} - Age: {self._age}"

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be beetwen 20 and 80")

    def get_age(self):
        return self._age


if __name__ == "__main__":
    p = Person("Robert", 30)

    print(p.display())
