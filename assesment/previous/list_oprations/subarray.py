def gensubarray():
     st = list(map(int,input("Enter the string ...").split()))
     target= int(input("enter the number ..."))
     i=0
     while i<len(st):
           s=[]
           j=i
           while j<len(st):
                 s.append(st[j])
                 if sum(s) == target:
                    print("Minimum size sub array is ",len(s))    
                 j+=1
           i+=1

