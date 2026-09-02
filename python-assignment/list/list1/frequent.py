'''6.

 Frequency Count of Elements (Advanced Scenario-Based Problem)


A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

The department wants to analyze:

* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)

---

 Requirements

Write a Python program to:

1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary

## Input

[1, 2, 2, 3, 3, 3, 4, 1, 2]

## Output


Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1

Most Frequent: 2 or 3 (tie)
Least Frequent: 4'''

n=list(map(int,input("## Input:").split()))
l=n
e=[]
count=0
for i in n:
	if i not in e:
		e.append(i)
		count=count+1
print(e)
print(count)


























