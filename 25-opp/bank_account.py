class BankAccount:
    # def __init__(self, name, balance=0):
    # self.name = name
    # self.balance = balance

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
    a1 = BankAccount()
    a1.set_details("Ramón",600)
    a2 = BankAccount()
    a2.set_details("Tom")

    print(a1.display())
    print(a2.display())

    a1.withdraw(100)
    a2.deposit(500)

    print(a1.display())
    print(a2.display())
