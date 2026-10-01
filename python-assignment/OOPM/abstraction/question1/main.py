from question1.payment.payment import (
    UPIPayment,
    CreditCardPayment,
    DebitCardPayment,
    NetBankingPayment,
    WalletPayment
)


obj = None

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

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            Customer_Name = input("Enter Customer Name: ")
            Order_ID = int(input("Enter Order ID: "))
            order_fee = int(input("Enter Order Fee: "))

            while True:
                print("""
                Select Payment Method

                1. UPI
                2. Credit Card
                3. Debit Card
                4. Net Banking
                5. Wallet
                6. Back to Main Menu
                """)

                a = int(input("Enter your choice: "))

                match a:

                    case 1:
                        UPI_ID = input("Enter the UPI ID: ")
                        UPI_PIN = input("Enter the UPI PIN: ")

                        obj = UPIPayment(
                            UPI_ID,
                            UPI_PIN,
                            Customer_Name,
                            Order_ID,
                            order_fee
                        )

                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()

                    case 2:
                        Card_Number = input("Enter the Card Number: ")
                        Card_Holder_Name = input("Enter the Card Holder Name: ")
                        CVV = input("Enter the CVV: ")
                        Expiry_Date = input("Enter the Expiry Date: ")

                        obj = CreditCardPayment(
                            Card_Number,
                            Card_Holder_Name,
                            CVV,
                            Expiry_Date,
                            Customer_Name,
                            Order_ID,
                            order_fee
                        )

                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()

                    case 3:
                        Card_Number = input("Enter the Card Number: ")
                        Card_Holder_Name = input("Enter the Card Holder Name: ")
                        CVV = input("Enter the CVV: ")
                        Expiry_Date = input("Enter the Expiry Date: ")

                        obj = DebitCardPayment(
                            Card_Number,
                            Card_Holder_Name,
                            CVV,
                            Expiry_Date,
                            Customer_Name,
                            Order_ID,
                            order_fee
                        )

                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()

                    case 4:
                        Bank_name = input("Enter the Bank Name: ")
                        Account_Number = input("Enter the Account Number: ")

                        obj = NetBankingPayment(
                            Bank_name,
                            Account_Number,
                            Customer_Name,
                            Order_ID,
                            order_fee
                        )

                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()

                    case 5:
                        Wallet_Name = input("Enter Wallet Name: ")
                        Mobile_Number = input("Enter Mobile Number: ")
                        Wallet_PIN = input("Enter Wallet PIN: ")

                        obj = WalletPayment(
                            Wallet_Name,
                            Mobile_Number,
                            Wallet_PIN,
                            Customer_Name,
                            Order_ID,
                            order_fee
                        )

                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()

                    case 6:
                        break

                    case _:
                        print("Invalid payment method")

        case 2:
            if obj:
                obj.generate_receipt()
            else:
                print("Please create a payment first.")

        case 3:
            print("EXIT")
            break

        case _:
            print("Invalid choice")