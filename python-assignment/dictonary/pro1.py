'''1.

=========================================
ONLINE SHOPPING CART
=========================================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

---'''
print("=========================================")
print("ONLINE SHOPPING CART")
print("=========================================")
n=int(input("enter the number of items here:"))
d={ }
s=0
for i in range(n):
	key=input(" Enter Product Name")
	value=int(input(" Quantity Purchased:"))
	d[key]=value
print(d.values( ))
v=list(d.values( ))
print("sum is:",sum(v))






 



