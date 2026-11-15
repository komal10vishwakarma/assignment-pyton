
from add import add
from add_product import add_product
from place_order import place_order
from display import display
from search import search
from updateproduct import updatepro
from updateorder import updateorder

while True:
    print("""
===== ONLINE SHOPPING ORDER MANAGEMENT =====
1. Add Customer
2. Add Product
3. Place Order
4. Display All Orders with Customer and Product Details
5. Search Customer by Name
6. Update Product Price
7. Update Order Status
8. Delete Order
9. Display Customer-wise Total Purchase Amount
10. Display Products Costing More Than Average Product Price
11. Display Customers Who Have Placed at Least One Order
12. Display Customers Who Have Not Placed Any Order
13. Exit
    """
)
    choice=int(input("enter you choice here ...."))
    if choice ==1:
        add()
    elif choice==2:
        add_product()
    elif choice==3:
        place_order()
    elif choice==4:
        display()
    elif choice==5:
        search()
    elif choice==6:
        updatepro()
    elif choice==7:
        updateorder()
    elif choice==8:    
        pass
    elif choice==9:
       pass
    elif choice==9:
       pass
    elif choice==10:
        pass
    elif choice==11:
        pass
    elif choice==12:
        pass
    elif choice==13:
        print("Exit")
    else:
        print("Invalid Choice")