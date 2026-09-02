'''Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''

s=input("enter your complaint").strip
word_count=0
for ch in s :
	if ch==" ":
		word_count=word_count+1
print(word_counter)