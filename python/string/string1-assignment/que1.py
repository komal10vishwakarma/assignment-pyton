'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8'''

st=input("enter the string:")
count=0
for ch in st.lower():
	if ch=='a' or ch== 'i' or ch=='o' or ch=='e' or ch=='u':
		count=count+1
          
	
print(count)
