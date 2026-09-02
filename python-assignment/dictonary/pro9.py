'''=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
'''
print("=========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("=========================================")
stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}
s=list(stock.values())
print(s)

for i in s:
	if i<=30:
		print(i)
		
for k ,v in stock.items():
	if i in stock:
		count>30
		
			print(k)
		
