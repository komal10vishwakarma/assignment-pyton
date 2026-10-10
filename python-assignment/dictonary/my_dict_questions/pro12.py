'''
2	Count word frequencies in a sentence.	Input: 'cat dog cat bird'	Output: {'cat':2,'dog':1,'bird':1}
'''
string=input("enter the string here:").split()
f={}
for i in string:
	f[i]=string.count(i)
print(f)

