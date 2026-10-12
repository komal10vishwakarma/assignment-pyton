'''
79	Divide a string into n equal parts.	S = "abcdef", n = 3	"ab", "cd", "ef"
'''
s=input("enter the string here:")
n=int(input("enter the number:"))
lenth=len(s)/n
if  "." in str(lenth) :
      print("not possible")
else:
	for i in range(lenth):
		for j in s:
			s=""
			print(s)
		
		

	
	