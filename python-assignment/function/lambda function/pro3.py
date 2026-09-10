pro=int(input("Enter the number of products:"))

prices=[]
for i in range(pro):
	prices.append(int(input()))

result=filter(lambda x:x>2000,prices)
print("Sample Output")
print("Discounted Prices:")
final=map(lambda x:x-x*0.20,result)
print(list(final))