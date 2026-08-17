'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy'''

s = input("Enter a string: ")
result = ""
space = False

for ch in s:
    if ch.isspace():
        if space == False:
            result = result + " "
            space = True
    else:
        result = result + ch
        space = False

print("Output:", result.strip())
	

