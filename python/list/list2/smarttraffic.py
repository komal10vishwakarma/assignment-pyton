'''2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5'''

n=list(map(int,input("elevation (input):").split()))
new=[]
peakindex=-1
for i in range(len(n)):
	if i==0:
		if len(n)==1 or n[i]>n[i+1]:
			peakindex=i
			new.append(n[i])	
			break
	elif i==len(n)-1:
		if n[i]>n[i-1]:
			peakindex=i
			new.append(n[i])	
			break
	else:
		if n[i]>n[i-1] and n[i]>n[i+1]:
			peakindex=i
			new.append(n[i])
			
print("peakindex",peakindex)
print("new list",new)
s=sum(new)
print("sum",s)
pro=1
for p in new:
	pro=pro*p
print("product is",pro)

for j in new:
	
			
















