# 6. Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

num = int(input("Enter a number: "))

if num < 0:
    num = -num

print(f"Absolute value:{num}")