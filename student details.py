class details:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display (self):
        print(self .name,"name")
        print(self.age,"age")
        print(self.course,"course")
name=input("enter the student name :")
age=int (input("enter the students age:"))
course= input("enter the course:")
A=details(name,age,course)
A.display()
