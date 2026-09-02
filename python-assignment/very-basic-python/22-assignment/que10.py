'''10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate'''

marks=int(input("enter the marks :"))
attendance=int(input("enter the attendence:"))
if marks >=40:
    print("Pass")
if attendance >= 75:
    print("Eligible for certificate")