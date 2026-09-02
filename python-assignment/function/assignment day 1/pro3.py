print("ONLINE SHOPPING SYSTEM")
print ("MENU")
print("1. Customer Registration")
print ("2. Product Information")
print("3. Generate Invoice")
print ("4. Add Multiple Products")
print("5. Display Customer Profile")
print ("6. Exit")

while True:
	choice=int(input("enter the choice here:"))
	match choice:
		case 1:
			def registration(name,Email,Mobile_number):
				print("Enter Name : ",name)
				print("Enter Email :",Email)	
				print("Enter Mobile :",Mobile_number)
			name=input("enter name:")
			Email=input("enter mail here:")
			Mobile_number=int(input("enter Mobile_number here:"))
			registration(name,Email,Mobile_number)
			print("Customer Registered Successfully")

		case 2:
			def proinfo(Product_Name, Price, Category):
				print("Product Name:",Product_Name)
				print("Price:",Price)
				print("Category:",Category)
			Price=int(input("enter the price here:"))
			Category=input("enter the category here:")
			Product_Name=input("enter the product name here:")
			proinfo(Price,Product_Name, Category)
			print("Product Details Displayed Successfully")

		case 3:

			def ef(Enter_Product_Name ,Enter_Price=0):
				print("Product Name:",Enter_Product_Name)
				print("Price:",Enter_Price)
			Enter_Product_Name =input("Enter the product name ")
			price  = input("Enter the price")
			ef(Enter_Product_Name ,price)
			ef(Enter_Product_Name)
			
			
				
		case 4:
			product=0
			def mp(*products):
				print("Enter Price:",products)
			n=int(input("enter the number of products:"))
			products=[]
			for i in range(n):
					products.append(int(input()))
			mp(products)
      			
		case 5:
			print("Customer Profile Displayed Successfully")
		case _:
			print("EXIT")			

			
			
		