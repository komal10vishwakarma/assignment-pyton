'''61	Count total alphabets, digits, and special characters.	S = "a1b!c2"	Alphabets: 3, Digits: 2, Special: 1'''
string=input("enter the string:").split()
special=0
alpha=0
digit=0
for i in string:
	for j in i:
		if j.isalpha():
			alpha=alpha+1
		elif j.isdigit():
			digit=digit+1
		else:
			special=special+1
print(	"Alphabets:",alpha)
print("Digits:",digit)
print("Special: ",special)