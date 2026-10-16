class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,"name")
        print(self.age ,"age")
name=input("enter the persons name:")
age=int(input("enter the persons age:"))
e=person(name,age)
e.display()


        
        
        