'''8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found'''

l=list(map(int,input("enter the list elements here:").split()))
for i in l:
	count=0
	for j in l:
		if i==j:
			count=count+1
if count>=2:
	print(j)


