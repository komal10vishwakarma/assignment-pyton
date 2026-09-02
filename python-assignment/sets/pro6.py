print("=========================================")
print("COMMON CHARACTER FINDER")
print("=========================================")

print("MENU:")
print("1. Enter First String")
print("2. Enter Second String")
print("3. Display Common Characters")
print("4. Count Common Characters")
print("5. Exit")
n=int(input("Enter Your Choice here"))
match n:
	case 1:
		string1 = set(input("Enter the string 1 here: "))
		print(string1)
	case 2:
		string2 = set(input("Enter the string 2 here: "))
		print(string2)
	case 3:
		string1 = set(input("Enter the string 1 here: "))
		print(string1)
		string2 = set(input("Enter the string 2 here: "))
		print(string2)
		print("Common Characters",string1.intersection(string2))
	case 4:
		string1 = set(input("Enter the string 1 here: "))
		print(string1)
		string2 = set(input("Enter the string 2 here: "))
		print(string2)
		
		print("Common Characters",string1.union(string2))
		string1.count(string1)
	case 5 :
		print("Exit")
		
		
		
