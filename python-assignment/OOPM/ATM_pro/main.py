class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()


    def menu(self):
        user_input=input("""
            HOW WOULD YOU LIKE TO PROCEED..?
            1-Enter 1 to create pin
            2-Enter 2 to deposit
            3-Enter 3 to withdraw
            4-Enter 4 to check balance
            5-Enter 5 to EXIT
        """)

        if user_input=="1":
            self.pin()
        if user_input=="2":
            self.deposite()
        if user_input=="3":
            self.withdraw()
        if user_input=="4":
            self.balance()
        if user_input=="5":
            print("EXIT")

    def pin(self):
        self.pin=int(input("enter the pin here:"))
        print("PIN IS SUCCESSFULLY CREATED")

    def deposite(self):
        temp=int(input("enter the pin"))
        if temp==self.pin:
            self.deposite=int(input("ENTER MONEY YOU WANT TO DEPOSITE"))
            self.balance=self.balance+self.deposite
            print("THE MONEY IS DEPOSITEd SUCCESSFULLY")

    def withdraw(self):
        temp=int(input("enter the pin"))
        if temp==self.pin:
            amount=int(input("enter the amont you want to withdraw"))
            if self.balance>=amount:
                self.balance=self.balance-amount
                print("OPERATION SWUCCESSFULL")
            else:
                print("SORRY...YOU DON'T HAVE THAT MUCH MONEY IN YOUR ACCOUNT")
        else:
            print("Invalid Pin")

    def balance(self):
        temp=int(input("enter the pin"))
        if temp==self.pin:
            print("BALANCE IS...",self.balance)
        else:
            print("Invalid Pin")


atm = Atm()


    