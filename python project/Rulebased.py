import random

print("Hi I Am AIBOT,How Can I Help You ...")

name=input("what is your name..?")
# user=input("enter what do you want me to do....")
print(f"Hello ,{name}" )
print(f"Select your choice from the following options ,{name}:")
while True:
 print("=" * 30)
 print("        MAIN MENU")
 print("=" * 30)
 print("1.chit chat")
 print("2.jokes")
 print("3.facts")
 print("4.basic tasks")
 print("5.riddles")
 print("6.motivational quotes")
 print("7.exit" )
 print("=" * 30)
 choice=int(input("enter your choice-----"))

 match choice:
     
  case 1:
   while True:

        user = input("You: ")

        if user.lower() == "bye" or user.lower() == "back" or user.lower() == "exit" or user.lower() == "menu":
            print("AIBOT: Returning to the main menu...")
           

        elif user.lower() == "hi" or user.lower() == "hii" or user.lower() == "hiii" or user.lower() == "hello" or user.lower() == "hlo" or user.lower() == "hello aibot" or user.lower() == "good morning" or user.lower() == "good afternoon" or user.lower() == "good evening":
            print(f"AIBOT: Hello, {name}! How can I help you?")
       

        elif user.lower() == "i am bored":
            print("AIBOT: Let's hear a joke or solve a riddle!")
           

        elif user.lower() == "are you a robot?":
            print("AIBOT: Yes! I'm a simple Python chatbot.")
   

        elif user.lower() == "can you help me":
            print("AIBOT: Of course! Choose an option from the menu, and I'll do my best.")

        elif user.lower() == "what is today's date":
            print("AIBOT: Sorry, I can't tell the current date yet.")

        elif user.lower() == "what is the time":
            print("AIBOT: Sorry, I can't tell the current time yet.")

        elif user.lower() == "who made you":
            print("AIBOT: I was created using Python.")

        elif user.lower() == "thank you":
            print("AIBOT: You're welcome!")

        else:
            print("AIBOT: Sorry, I can't understand you. Please try again.")
        choice = input("Do you want to continue this chat?(yes/no): ")
        if choice.lower() == "no":
         break
   
   
  case 2:
    while True:
    
     print("joke")
     print("-"*15)
     joke= random.randint(1,12)
     if joke==1:
        print("Why do pr5ogrammers prefer dark mode?\nBecause light attracts bugs!")
     elif joke==2:
        print(" Why did the programmer quit his job?\nBecause he didn't get arrays!")
     elif joke==3:
        print(" Why do Java developers wear glasses?\nBecause they don't C#.")
     elif joke==4:
        print("How many programmers does it take to change a light bulb?None. It's a hardware problem.")
     elif joke==5:
        print(" Why was the computer cold?Because it left its Windows open.")
     elif joke==6:
        print("Why did the programmer go broke?\nBecause he used up all his cache.")
     elif joke==7:
        print(" Why do programmers hate nature?\nIt has too many bugs.")
     elif joke==8:
        print(" Why did the computer visit the doctor?\nIt had a virus.")
     elif joke==9:
        print("What is a programmer's favorite place?\n The keyboard!")
     elif joke==10:
        print("Why was the computer so smart?\nBecause it listened to its motherboard.")
     elif joke==11:
        print("What did the programmer say after fixing the bug?\nIt works on my machine!")
     elif joke==12:
        print(" Why was the programmer always calm?\nBecause they knew how to handle exceptions!")
     choice = input("Do you want another joke? (yes/no): ")
     if choice.lower() == "no":
       break
  case 3:
    while True:

     print("facts")
     print("-"*15)
     fact=random.randint(1,10)
     
     if (fact == 1):
        print("Fact:The first computer programmer was Ada Lovelace.")
     elif( fact == 2):
        print("Fact:Python was released in 1991.")
     elif( fact == 3):
        print("Fact:Python is named after the comedy show Monty Python, not the snake.")
     elif( fact == 4):
        print("Fact:HTML is a markup language, not a programming language.")
     elif( fact == 5):
        print("Fact:Java and JavaScript are different programming languages.")
     elif( fact == 6):
        print("Fact :Computers understand only binary language (0 and 1).")
     elif( fact == 7):
        print("Fact :There are more than 700 programming languages.")

     elif( fact == 8):
        print("Fact :This is the first program many beginners write.")

     elif( fact == 9):
        print("Fact :Debugging means finding and fixing errors in code.")

     elif( fact == 10):
        print("Fact :Google, YouTube, Instagram, and Spotify use Python.")
     choice = input("Do you want another fact? (yes/no): ")
     if choice.lower() == "no":
        break  
  case 4:
    while True:
      
      print("basic tasks")
      print("-"*15)
      print("1.square")
      print("2.cube")
      print("3.palindrom")
      print("4.Even and Odd")
      print("5.Factorial")
      print("6.Exit")
      print("-"*15)
      n = input("enter the number")
      match n:
        case "1":
          number = int(input("enter the number"))
          square = number**2
          print("Square is:", square)
        case "2":
          number = int(input("enter the number"))
          cube = number**3
          print("Cube is:", cube)
        case "3":
          number = int(input("enter the number"))
          temp = number
          rev = 0
          while number > 0:
            rev = rev * 10 + number % 10
            number = number // 10
          if rev == temp:
            print("Palindrom")
          else:
            print("Number is not palindrome")
        case "4":
          number = int(input("enter the number"))
          if number % 2 == 0:
            print("Number is even")
          else:
            print("Number is odd")
        case "5":
          number = int(input("enter the number"))
          fact = 1
          for i in range(number, 0, -1):
            fact = fact * i
          print("Factorial is:", fact)
        case "6":
          print("you exit from the loop")
          break
        case _:
          print("Invalid choice. Please try again.")
          
  case 5:
    while True:
    
     print("----riddles----")
     print("-"*15)
     riddle=random.randint(1,10)
     if riddle==1:
        print("Riddle:What has keys but can't open locks?")
        answer=input("enter your anser:")
        if answer.lower()=="keyboard":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 2:
        print("Riddle :What has hands but can't clap?")
        answer=input("enter your anser:")
        if answer.lower()=="clock":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 3:
        print("Riddle:What gets wetter the more it dries?")
        answer=input("enter your anser:")
        if answer.lower()=="towel":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 4:
        print("Riddle:What has one eye but cannot see?")
        answer=input("enter your anser:")
        if answer.lower()=="needle":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 5:
        print("Riddle:What comes down but never goes up?")
        answer=input("enter your anser:")
        if answer.lower()=="rain":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 6:
        print("Riddle :What has many teeth but cannot bite?")
        answer=input("enter your anser:")
        if answer.lower()=="comb":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 7:
        print("Riddle:What can travel around the world while staying in one place?")
        answer=input("enter your anser:")
        if answer.lower()=="keyboard":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 8:
        print("Riddle :What has a neck but no head?")
        answer=input("enter your anser:")
        if answer.lower()=="bottle":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 9:
        print("Riddle:What has four legs but cannot walk?")
        answer=input("enter your anser:")
        if answer.lower()=="table":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")

     elif riddle== 10:
        print("Riddle :What goes up but never comes down?")
        answer=input("enter your anser:")
        if answer.lower()=="your age":
            print("congratulations!you are right...")
        else:
            print("Oops! try again")
     choice = input("Do you want another fact? (yes/no): ")
     if choice.lower() == "no":
      break
     
  case 6:
    while True:
      print("---motivational quotes---")
      print("-"*15)
      quote=random.randint(1,10)
      if quote==1:
        print("Quote:Believe you can and you're halfway there")
      elif quote==2:
        print("Quote:Your limitation—it's only your imagination.")
      elif quote==3:
        print("Quote:Push yourself, because no one else is going to do it for you.")
      elif quote==4:
        print("Quote:Great things never come from comfort zones.")
      elif quote==5:
        print("Quote:Dream it. Wish it. Do it.")
      elif quote==6:
        print("Quote:Success doesn't just find you. You have to go out and get it.")
      elif quote==7:
        print("Quote:The harder you work for something, the greater you'll feel when you achieve it.")
      elif quote==8:
        print("Quote:Dream bigger. Do bigger.")
      elif quote==9:
        print("Quote:Don't stop when you're tired. Stop when you're done.")
      elif quote==10:
        print("Quote:Wake up with determination. Go to bed with satisfaction.")
      choice = input("Do you want another motivational quotes ? (yes/no): ")
      if choice.lower() == "no":
        break
  case 7:
        print("exit")
        break


continue_choice = input("Do you want to continue? (yes/no): ")
if continue_choice.lower() == "no":
  print("Thank you for using AIBOT. Have a nice day!")
 
