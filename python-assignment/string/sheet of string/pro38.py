'''
38	Reverse words without split().	S = "a b c"	"c b a"
'''
s=input("enter the string here:")
rev=""
l=len(s)
for i in s:
	rev=i+rev
print(rev)