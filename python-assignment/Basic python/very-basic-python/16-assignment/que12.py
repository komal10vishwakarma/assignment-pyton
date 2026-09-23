amount = int(input("Enter amount: "))

notes100 = amount // 100
amount = amount % 100

notes50 = amount // 50
amount = amount % 50

notes10 = amount // 10

print("₹100 notes =", notes100)
print("₹50 notes =", notes50)
print("₹10 notes =", notes10)