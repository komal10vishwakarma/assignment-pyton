



while True:
    print("""
------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit
    """)
    choice=input("enter you choice:")
    match choice:
        case 1:

            while True:
                print("""
                Select Payment Method

                        1. UPI
                        2. Credit Card
                        3. Debit Card
                        4. Net Banking
                        5. Wallet
                """)
                a=int(input("Enter your choice:"))
                match a:
                    case 1:
                        pass

        case 2:
            pass

        case 3:
            print("EXIT")

        case __:
            print("Invalid choice")

