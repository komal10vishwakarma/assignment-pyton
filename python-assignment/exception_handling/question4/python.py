print("BANK ACCOUNT MANAGEMENT SYSTEM")


class InsufficientBalanceException(Exception):
    pass 
class NegativeDepositException(Exception):
    pass 
class InvalidWithdrawalException(Exception):
    pass
class InvalidAmountException(Exception):
    pass
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount<0:
            raise NegativeDepositException
        elif amount==0:
            raise InvalidAmountException
        self.balance=self.balance+amount
        return balance
    def withdraw(self,amount):
        if amount<0:
            raise InvalidWithdrawalException
        elif amount==0:
            raise InvalidAmountException
        elif amount > self.balance:
            raise InsufficientBalanceException
        self.balance=self.balance-amount
        return balance      
    
    def check_balance(self):
        print("Available Balance:", self.balance)
       
    def display_account_details(self):
        print("Account Number:",self.account_number)
        print("Account Holder:",self.account_holder)
        print("Available Balance:",self.balance)
account_number=(input("enter the account number here:"))
account_holder=(input("enter the holder name:"))
balance=int(input("enter the balance here:"))
BankAccount(account_number,account_holder,balance)
obj=BankAccount(
    account_number,account_holder,balance
)
try:
    
except:
    pass



