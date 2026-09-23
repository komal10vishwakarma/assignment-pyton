class Account():
    def __init__(self,account_number,customer_name,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance

    def display_account(self,Account,account_number,customer_name,balance):
        super(). __init__(account_number,customer_name,balance)

    def deposit(self,balance):
             self.balance+=balance

    def withdraw(self):
        if balance<self.balance:
            self.balance-=balance
        else:
            print("bhai tere paas to paise hi nhi h sale gareeb")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,price):
        self.__balance=price
        

    @balance.deleter
    def balance(self):
        del self.__balance

    
class Savingsaccount(Account):
    def __init__(self,interest_rate,account_number,customer_name,balance):
        print(interest_rate,account_number,customer_name,balance)
        super(). __init__(account_number,customer_name,balance)
        self.interest_rate=interest_rate

    def display_account(self):
        print(interest_rate,account_number,customer_name,balance)

    
class PremiumSavingsAccount(Savingsaccount):
    def __init__(self,cashback_percentage,interest_rate,account_number,customer_name,balance):
        super().__init__(interest_rate,account_number,customer_name,balance)
        self.cashback_percentage=cashback_percentage
    def display_account(self):
        print(interest_rate,account_number,customer_name,balance)

account_number=int(input("Enter Account Number:"))
customer_name=input("Enter Customer Name:")
balance=int(input("Enter Initial Balance:"))
cashback_percentage=int(input("enter cashback percentage here"))
interest_rate=int(input("enter interest_rate here"))
print("""what account type is yours" 
        1-  Savingsaccount
        2-  PremiumSavingsAccount """)


choice=int(input("enter the account type...1 or 2"))
if choice==1:
    obj=Savingsaccount(interest_rate,account_number,customer_name,balance)
    obj.display_account()

elif choice==2:
    obj=PremiumSavingsAccount(cashback_percentage,interest_rate,account_number,customer_name,balance)
    obj.display_account()