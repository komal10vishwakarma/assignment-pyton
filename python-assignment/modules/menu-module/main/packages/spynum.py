from .sumofdigits import s
def spy(n):
	add=s(n)
	print(add)
	num=str(n)
	pro=1
	for i in num:
		pro=pro*int(i)
	print(pro)
	if add==pro:
		print("Spy Number")
	else:
		print("Not Spy Number")
	return spy