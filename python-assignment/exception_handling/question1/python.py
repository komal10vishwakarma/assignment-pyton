class InvalidQuantityException(Exception):
    pass



class Book:
    def __init__(self,book_id,book_title,author_name,price,quantity     ):
        self.book_id=book_id
        self.book_title =book_title 
        self.author_name=author_name
        self.price =price 
        self.quantity =quantity 
    def purchase(self,quantity):
        if quantity<=0:
            raise InvalidQuantityException("quantity should be positive")
        elif quantity>self.quantity:
            raise InvalidQuantityException(" Quantity not available")
        self.quantity=self.quantity-quantity
        print("remian quantity is :",self.quantity)
        
book_id= input("Enter book id here")
book_title =input("enter book title here:")
author_name=input("enter author name  here:")
price =float(input("enter the price of the book"))
quantity=int(input("enter the quantity here:"))
available_quantity = int(input("Enter Available Quantity: "))
purchase_quantity = int(input("Enter Quantity to Purchase: "))

obj=Book(
    book_id,book_title,author_name,price,quantity
)

try:
    obj.purchase(purchase_quantity)
except InvalidQuantityException as e:
    print("InvalidQuantityException:", e)