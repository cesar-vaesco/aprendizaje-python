class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        return f"Name: {self.name} - Balance: {self.balance}"

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


if "__main__" == __name__:
    a1 = BankAccount("Ramón", 600)
    a2 = BankAccount("Tom")

    print(a1.display())
    print(a2.display())

    a1.withdraw(100)
    a2.deposit(500)
    a2.withdraw(250)

    print(a1.display())
    print(a2.display())
