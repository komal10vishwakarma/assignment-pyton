'''
*
* *
*  *
*   *
* * * * *
'''

n = int(input("no."))
i = 1
while i <= n:
	j = 1
	while j <=i:
		if j == i or j == 1 or i == n:
			print("*",end="")
			j+=1
		else:
			print(" ",end="" )
			j+=1
		
	print()
	i+=1
	
