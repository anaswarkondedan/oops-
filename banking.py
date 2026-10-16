class money:
    def __init__(self,balance):
        self.balance= balance

    def deposit(self,amount):
            self.balance += amount

    def withdraw(self,amount):
        if amount<=self.balance:
          self.balance -= amount
          print("amount dithdraw",amount)
        else:              
            print("insufficient balance")

    def check_balance(self,):
        print("account balance",self.balance)

balance = int(input("Enter the initial balance: "))

e=money(balance)

amount = int(input("Enter the amount to deposit: "))
e.deposit(amount)

amount = int(input("Enter the amount to withdraw: "))
e.withdraw(amount)
e.check_balance()
                         

a
        


        
