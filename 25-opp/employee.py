

class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    #  Se puede leer el valor pero no hay método setter, no se podría cambiar el valor
    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    # Se puede cambiar la contraseña pero no se puede leer
    @property
    def password(self):
        raise AttributeError("password not readable")

    @password.setter
    def password(self, password):
        self._password = password

    # Se puede ver y cambiar el salario
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def display(self):
        return f"Name: {self.name} - Salary: {self.salary}"


employee1 = Employee("Richard", "1245", 5500)

# employee1.name = "Juan"
# print(employee1.password)

print(employee1.display())

employee1.salary= 4500
# print(employee1.password)
print(employee1.display())
