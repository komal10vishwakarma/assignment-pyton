'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e'''
s=input("Input:").strip()
visited=input("")
count=0
for ch in s:
	if ch in visited:
		continue
	else:
		if 1 ==s.count(ch):
			print(ch)
			visited+=ch
			break
			
	
	

