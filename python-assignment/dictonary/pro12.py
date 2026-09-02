'''=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
'''
print("=========================================")
print("ONLINE FOOD DELIVERY ANALYSIS")
print("=========================================")
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
d={}
for i in orders:
	d[i]=d.get(i,0)+1
print(d)
t=(max(d,key=d.get))
print("Most Ordered  :",t)