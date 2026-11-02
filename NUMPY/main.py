import numpy as np

a=np.array([5])
print(a)

print(type(a))
b=np.zeros(5,dtype=int)
print(b)

c=np.full(5,7)
print(c)

d=np.full(5,'komal')
print(d)

e=np.arange(1,11)
print(e)

f=np.linspace(0,10,5)
print(f)
#starting point,ending point,how many values you want ----fir equal values aayenge jitni chahiye utni 

g=np.array([[1,2,3],
           [4,5,6,],
           [7,8,9]])
print(g)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


h=np.eye(3,dtype=int)
print(h)
# y bhai diagonal m 1 denge,,,,or hamesha ek square metix generate hogi by default 
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

i=np.zeros([2,3],dtype=int)
print(i) #fir first wala row,seconf=d wala column de raha h...and y xzer matrix dega
# [[0 0 0]
#  [0 0 0]]

