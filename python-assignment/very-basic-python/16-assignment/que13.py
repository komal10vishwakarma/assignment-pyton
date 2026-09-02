p=int(input("enter the value of principle"))
r=int(input("enter the value of rate"))
t=int(input("enter the value of time"))
amount=(p(1+r/100)**t)
CI=amount-p
print("amount",amount)
print("CI",CI)
