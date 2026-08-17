'''x = [1, 2, 3, 4]
match x:
    case [a, b, *c]:
        print(a, b, c)
    case _:
        print("Invalid")
x = [10, 20, 30, 40]
match x:
    case [10, *rest]:
        print(rest)
    case _
        print("No")

n = 5 
while n > 1: 
	if n % 2 == 0:
		n -= 2 
	else: 
		n -= 1 
print(n)

x = True + True * 2 
print(x, type(x))'''
'''
a = [1, 2] 
b = a 
c = a[:] 

b.append(3) 
print(a, b, c, a is b, a is c)'''
'''
x = (1, 2, [3, 4]) 
x[2].append(5) 
print(x)'''
'''
x = [10, 20, 30, 40, 50] 
print(x[4:0:-2])'''
a = [1, 2, 3] 
b = a 
b = b + [4] 
print(a, b, a is b)

x = [1, 2, 3] 
a, *b = x 
print(type(b), b)

x = [[0] * 2] * 3 
x[0][0] = 9 
print(x)
























