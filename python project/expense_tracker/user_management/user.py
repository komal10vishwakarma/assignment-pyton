from expense_tracker..user import add_user
def add_user():
    u=[]
    user=input("enter your name")
    if user not in u:
        u.append(user)
    else:
        print("welcome")

def login_user():
    add_user()
    