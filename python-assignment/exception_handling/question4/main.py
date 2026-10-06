
while True():
    print("""
================================
BANK ACCOUNT SYSTEM
===================
1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit
   """)
    choice=int(input("enter you choice here:"))
    match choice:
        case 1:
            pass 
        case 2:
            pass
        case 3:
            pass 
        case 4:
            pass 
        case 5:
            print("Exit")
            break
        case __:
            print("invalid choice")