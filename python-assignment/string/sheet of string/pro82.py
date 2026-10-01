'''82	Create a string from a character array.	Char[] = {'h', 'i'}	"hi"'''
s = input("Enter the characters: ")

string = ""

for i in s:
    string = string + i

print(string)
