class temp:
    def __init__(self,celsius,faranheat):
        self.celsius=celsius
        self.faranheat=faranheat

    def cel(self):
        print(self.celsius,"celsius")
        abc=(self.celsius*9/5)+32

        print("faranheat:",abc)
                         
                         
        self.celsius=self.celsius+abc

    def far(self):
        print(self.faranheat,"faranheat")
        bcd=(self.faranheat-32 )* 5/9
        print("celsius",bcd)

celsius = int(input("Enter the celsius: "))
faranheat = int(input("Enter the fahrenheit: "))
e=temp(celsius,faranheat)


e.cel()
e.far()


        




     

    

        