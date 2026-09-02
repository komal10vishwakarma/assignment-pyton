'''30	Replace a word with another word.	S = "old data", Old="old", New="new"	"new data"  '''
string=input("enter the string:").split()
word=input("enter the word that you want to replace:")
newword=input("enter the replace word here:")
c=" "
for i in string:
	if i!=word:
		c=c+i
	else :
		c=c + " "+newword
print("the new string is:",c,end=" ")
		
	
