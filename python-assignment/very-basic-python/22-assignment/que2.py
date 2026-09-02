'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction'''

marks=int(input("enter the marks:"))
if marks>=40:
    
        if marks>=75:
             print("Distinction")
        else:
             print("pass")
else:
    print("failed")