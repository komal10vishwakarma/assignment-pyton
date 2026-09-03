'''
60	Append two strings but remove adjacent duplicates.	S1="miss", S2="issippi"	"misisipi
'''
s1=input("enter the string1 here:")
s2=input("enter the string 2 here:")
string1=""
string2=""
for i in s1:
	if i not in string1:
		string1=string1+i

for j in s2:
	if j not in string2:
		string2=string2+j


main_string=string1+string2
print("OUTPUT:",main_string)
		
		