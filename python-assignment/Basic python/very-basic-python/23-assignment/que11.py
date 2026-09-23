

distance=int(input("enter the distance "))
cl=input("enter your travel class")

if distance<=100 :
     if cl.lower()=="Sleeper":
        print("₹100")
     else:
        print("₹200")
   
  
elif distance>=101 and distance<500:
     if cl.lower()=="Sleeper":
        print("₹300")
     else:
        print("₹600")
  

elif distance>5000 :
     if cl.lower()=="Sleeper":
        print("₹500")
     else:
        print("₹1000")
 

   