class employe:
 
 def __init__(self,salary):
    self.salary=salary
 def increase_salary(self,persentage):
      total=self.salary *persentage/100
      self.salary=self.salary+total

 def define(self):
        print(self.salary,"updated salary")
        
        

salary=int(input("enter the salary:"))
persentage=int(input("enter the percentage:"))


e = employe(salary)

e.increase_salary(persentage)
e.define()







      


    

      
    

