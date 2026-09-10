n=int(input("Enter the number of students:"))
print(n)
marks=[]
for i in range(n):
	marks.append(int(input()))
print(marks)

result=filter(lambda x:x>75,marks)
result=list(result)


print("Sample Output")
print("Scholarship Marks:")

bonus = map(lambda x:x+5,result)
print(list(bonus))

final_output=sorted(bonus,key=lambda x:x,reverse=True)
print("final_output")
