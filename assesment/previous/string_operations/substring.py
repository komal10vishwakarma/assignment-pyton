def gensubtring():
     st = input("Enter the string ...")
     i=0
     while i<len(st):
           s=""
           j=i
           while j<len(st):
                 s+=st[j]
                 print(s)
                 j+=1
           i+=1
           