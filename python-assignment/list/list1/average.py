'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []'''

s=list(map(int,input("enter the salaries here:").split()))
r=s
remaining_list = []
total=len(r)
overall=sum(s)
average=(overall/total)
print (" Average = ",average)

	
	





