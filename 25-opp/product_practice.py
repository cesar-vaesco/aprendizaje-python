class Product_Practice:
    def __init__(self, id, marked_price, discount) -> None:
        self.id = id
        self.marked_price = marked_price
        self.discount = discount

    @property
    def selling_price(self):
        return self.marked_price - 0.01 * self.discount * self.marked_price


    def display(self):
        return f"Id: {self.id} - Marked_price: {self.marked_price} - Discount: {self.discount}"

    def display_selling_price(self):
        return f"Id: {self.id}  Selling_price: {self.selling_price}"

if "__main__" == __name__:
    p1 = Product_Practice('X879', 400, 6)
    p2 = Product_Practice('A234', 100, 5)
    p3 = Product_Practice('B987', 990, 4)
    p4 = Product_Practice('H456', 800, 6)

    print(p1.display())
    print(p2.display())
    print(p3.display())
    print(p4.display())
    
    print(p1.display_selling_price())
    print(p2.display_selling_price())
    print(p3.display_selling_price())
    print(p4.display_selling_price())

    p4.discount = 10
    print(p4.display_selling_price())