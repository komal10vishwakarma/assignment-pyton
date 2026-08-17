'''45	Check whether a string starts/ends with another string.	S = "apple pie", Prefix = "apple", Suffix =
"pie"	Start: True, End: True
'''

string=input("enter the string here:").split()
preffix=input("enter the prefix word here:")
suffix=input("enter the suffix here:")
if preffix!=suffix:
	print("Start: True, End: True")
else:
	print("Start : End : Similar")

		