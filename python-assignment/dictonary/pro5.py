'''=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}
'''
print("=========================================")
print("WORD LENGTH GROUPING")
print("=========================================")
tags = ["python","java","api","react","html","css"]
d={ }
for i in tags:
	l=len(i)
	if l not in d:
		d[l]=[]
	d[l].append(i)
print(d)
	
		
	