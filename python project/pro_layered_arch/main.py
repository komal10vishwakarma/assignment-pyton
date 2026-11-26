




while True:
    print("""
1-User RFegistration
2-User Login
3-Exit
    """)
    try:
        choice=int(input("Enter Your Choice Here-----"))
    except ValueError:
        print("Enter Choice Correctly...")
        continue
    if choice==1:
        while True:
            print("""
USER DASHBOARD
1-Report Lost Item
2-Report Found Item
3-View Lost Items
4-View Found Items
5-Search Items
6-View My Reports
7-Submit Claim
8-View My Claims
            """)
            try:
                choice=int(input("Enter Your Choice..."))
                if choice==1:
                    pass
                elif choice==2:
                    pass
                elif choice==3:
                    pass
                elif choice==4:
                    pass
                elif choice==5:
                    pass
                elif choice==6:
                    pass
                elif choice==7:
                    pass
                elif choice==7:
                    pass
                elif choice==7:
                    pass
                
            except ValueError:
                print("Enter Choice Correctly")
 
    elif choice==2:
        pass

    elif choice==3:
        pass 
    
    else:
        print("Invalid Choice")