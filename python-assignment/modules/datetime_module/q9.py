# 9. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).
character = input("Enter character: ")

if 'a'<= character <= 'z':
    print("It is lowercase")
elif 'A' <= character <= 'Z':
    print("It is uppercase")
else:
    print("It is not a letter")