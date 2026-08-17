
print("=========================================")
print("WEBSITE VISITOR TRACKING SYSTEM".center(41))
print("=========================================")

print("MENU:")
print("1. Add Visitor")
print("2. Remove Visitor")
print("3. Check Visitor")
print("4. Display All Visitors")
print("5. Count Unique Visitors")
print("6. Clear Visitor Data")
print("7. Exit")
visitors = set()
visitors.add(id)
print(visitors)
n=int(input("Enter Your Choice: "))
match n:
	case 1:
		id = input("Enter Visitor ID: ")
		visitors = set()
		visitors.add(id)
		print(visitors)
	case 2:
		id = input("Enter Visitor ID: ")

       		if id in visitors:
            		visitors.remove(id)
          		print("Visitor Removed")
       		 else:
          		print("Visitor Not Found")
	case 3:
		id = input("Enter Visitor ID: ")
		if id in visitors:
			print("Yes")
		else:
			print("No")
		
	case 4:
		print("All Visitors",visitors)	
	case 5:
		
		print("Lenght Of Visitors Is:",len(visitors))
	
	case 6:
		print(visitors.clear())
		print("Visitor Data Cleared")
		print(visitors)
	case 7:
		print("Exit")

	

	
	
	
