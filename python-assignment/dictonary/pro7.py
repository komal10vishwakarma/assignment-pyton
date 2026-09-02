'''=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi
'''
print("=========================================")
print("ONLINE EXAM RESULT SYSTEM")
print("=========================================")
result = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}
marks=list(result.values())
for m in marks:
	if m>=50:
		continue
for k ,v in result.items():
	if v!=m:
		print(k)
		continue
		
