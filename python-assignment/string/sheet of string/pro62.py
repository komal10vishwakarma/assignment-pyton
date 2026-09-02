'''62	Count vowels and consonants.	S = "apple"	Vowels: 2, Consonants: 3'''
string=input("Enter the string here:").split()
vowel=0
con=0
c=" "
for i in string:
	for j in i:
		if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' :
			vowel=vowel+1
		else:
			con=con+1
print("Vowels:",vowel)
print("Consonants:",con)
			