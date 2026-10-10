'''
1	Count character frequencies in a string.	Input: 'aabbc'	Output: {'a':2,'b':2,'c':1}'''
string=input("enter the string here:")
f={}
for i in string:
      f[i]=string.count(i)

print(f)
     
      
	
	