class MyClass:
    a = 5

    def __init__(self, x):
        self.x = x

    def method1(self):
        return f"x: {self.x}"

    @classmethod
    def method2(cls):
        return f"cls.a: {cls.a}"
    



mc1 = MyClass(10)

print(mc1.method1())
print(MyClass.method2())
print(mc1.method2())