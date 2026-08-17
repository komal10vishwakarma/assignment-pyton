'''l1=[1,2,3,4,5]
print(l1[2:])
print(l1[:2])
print(l1[:-1])
print(l1*2)
print(l1.pop(1))
print(list("a#b#c#d".split('#')))'''
'''
list1 = [1, 3] 
list2 = list1 
list1[0] = 4 
print(list2)'''

'''veggies = ['carrot', 'broccoli', 'potato', 'asparagus'] veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)'''

'''m = [x, y] 
for x in range(0, 4):
	for y in range(0, 4):
print(m)'''

'''points = [[1, 2], [3, 1.5], [0.5, 0.5]] 
points.sort() 
print(points)'''

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0] 
for lst in values: 
	for element in lst: 
			if v > element: 
				v = element 
print(v)