class store:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
       print(self.name,"name:")
       print(self.price,"price:")
       print(self.quantity,"quantity")
       total= self.price * self.quantity
       print("total price:",total)
name=input("enter the name:")
price=int(input("enter the price:"))
quantity= int(input("enter the quantity:"))

e=store(name,price,quantity)
e.display()
        
            
        