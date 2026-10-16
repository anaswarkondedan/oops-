class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book title:", self.title)
        print("Book author:", self.author)
        print("Book price:", self.price)

title = input("Enter the book title: ")
author = input("Enter the author: ")
price = int(input("Enter the price: "))

e = Book(title, author, price)
e.display()


        