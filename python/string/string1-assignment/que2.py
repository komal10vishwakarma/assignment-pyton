'''pace Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''

st=input("enter the input string:")
space=0
for ch in st.lower():

	if ch == " ":
		space=space+1
print(space)
