'''
Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them'''

num=list(map(int,input("enter the values:").split()))
p = []
pn = []
count= 0
count1=0
for i in num:
	for j in (2,int(i-1)):
		if i%j==0:
			count1=count1+1
			pn.append(i)
			break
	else:
		p.append(i)
		count=count+1
s = sorted(p)
print(p)
print(pn)
#l = s[-1]
print(" all prime numbers",p)
print("total prime numbers",count)
print("total non-prime numbers",count1)
#print("the largest prime number from the List:",l)
print("the prime numbers in ascending order:",s)

		