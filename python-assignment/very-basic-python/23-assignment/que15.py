stock =  int(input("enter number of stocks : "))
priority = input("enter priority (high/low)").lower()
distance = int(input("enter distance : "))

if stock >= 100 :
    if priority == "high" :
        if distance <=200 :
            dispatch = "immediately"
        else:
            dispatch = "fast courier"
    else:
        if stock >= 300 :
            dispatch = "bulk dispatch"
        else :
            dispatch = "normal dispatch"
else :
    if stock >= 50 and priority == "high" :
        dispatch = "partially dispatch"
    elif stock < 50 and priority == "high" :
        dispatch = "hold"
    else :
        dispatch = "out of stock"

print("dispatch status = ",dispatch