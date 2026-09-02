'''3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0'''


n=list(map(int,input("enter the INPUT:").split()))
e=[]
l=len(n)
peakindex=-1
sum=0
for i in range(l):
	if i==0:
		if l==1 or n[i]>n[i+1]:
			peakindex=i
			e.append(n[i])
			
	elif i==l-1:
		if n[i]>n[i-1]:
			peakindex=i
			e.append(n[i])
			
	else:
		
		if n[i]>n[i-1] and n[i]>n[i+1]:
			peakindex=i	
			e.append(n[i])
			
print("Peaks =:",e)
for s in e:
	sum=sum+s
print(sum)
print("Sum of squares = ",sum*sum)
f=sum/l
print("Average =:",f)



			
			