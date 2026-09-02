'''=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
'''
print("'=========================================")
print("MOBILE APP DOWNLOAD COUNTER")
print("'=========================================")
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
d={}
for i in cities:
	d[i]=d.get(i,0)+1		
print(d)
print("Most Downloads :",max(d,key=d.get))


