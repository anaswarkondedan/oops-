
class mobile:
    def __init__(self, mobile1, price1, mobile2, price2,
                 mobile3, price3, mobile4, price4, mobile5, price5):
        self.mobile1 = mobile1
        self.price1 = price1
        self.mobile2 = mobile2
        self.price2 = price2
        self.mobile3 = mobile3
        self.price3 = price3
        self.mobile4 = mobile4
        self.price4 = price4
        self.mobile5 = mobile5
        self.price5 = price5

    def display(self):
        if self.price1 > 20000:
            print("Mobile:", self.mobile1, "Price:", self.price1)
        if self.price2 > 20000:
            print("Mobile:", self.mobile2, "Price:", self.price2)
        if self.price3 > 20000:
            print("Mobile:", self.mobile3, "Price:", self.price3)
        if self.price4 > 20000:
            print("Mobile:", self.mobile4, "Price:", self.price4)
        if self.price5 > 20000:
            print("Mobile:", self.mobile5, "Price:", self.price5)


mobile1 = input("Enter the mobile name: ")
price1 = int(input("Enter the price: "))
mobile2 = input("Enter the mobile name: ")
price2 = int(input("Enter the price: "))
mobile3 = input("Enter the mobile name: ")
price3 = int(input("Enter the price: "))
mobile4 = input("Enter the mobile name: ")
price4 = int(input("Enter the price: "))
mobile5 = input("Enter the mobile name: ")
price5 = int(input("Enter the price: "))

i = mobile(mobile1, price1, mobile2, price2, mobile3, price3,
           mobile4, price4, mobile5, price5)
i.display()
