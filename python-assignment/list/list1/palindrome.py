'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''

n=list(map(int,input("enter the list items:").split()))
p = []
count = 0
rev=0
for i in n:
	q =i
	while q >= 0 :
		rev=rev*10+i%10
		q = q//10
	if rev == i :
		p.append(i)
		count+=1
r = sorted(p)
l = r[-1]
print("Palindromes:",p)
print("count:",count)
print("Largest:",l)
print("Sorted:",s)
	
	

