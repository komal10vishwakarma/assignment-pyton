'''4.

Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

Test Case 2

Input:
6
-1 0 -5 0 -2 -3

Output:
-1

Test Case 3

Input:
5
10 20 30 40 50

Processing:
Filtered array:
[10, 20, 30, 40, 50]

Leaders:
[50]

Output:
50'''


n=int(input("enter the size of element you want in the list:"))
arr=[]
e=[]

for i in range(n):
	arr.append(int(input()))
print(arr)
peakindex=-2
l=len(arr)
fillered_array=[]
for g in arr :
	if g>0 :
		fillered_array.append(g)
print("Filtered array:",fillered_array)
for i in range(l):
	if i==0:
		if l==1 or arr[i]>arr[i+1]:
			peakindex=i	
			e.append(arr[i])
	elif i==l-1 :
		if arr[i]>arr[i-1]:
			peakindex=i
			e.append(arr[i])
	else:
		if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
			peakindex=i 
			e.append(arr[i])
print("Leaders:",e)
print("sum is:",sum(e))






