'''
20	Find the second largest element.	[10, 40, 20, 50, 30]	40
'''
l1=list(map(int,input("enter the list element:").split()))
l1.sort()
print(l1[-2])