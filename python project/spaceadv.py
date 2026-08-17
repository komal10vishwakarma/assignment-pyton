import random
while True:
 print("="*30)
 print("Welcome to Space Adventure!")
 print("="*30)
 print("1.Moon")
 print("2.Mars")
 print("3.Jupiter")
 print("4.Saturn")
 print("5.Exit")
 des=int(input("Choose Your Destination"))
 match des:

    case 1 :
     print("You landed on the Moon!")
     des=random.randint(1, 3)
     if des==1:
      print("Fun Fact:The Moon has no atmosphere.")
     elif des==2:
        print("Are You Ready For The Quiz...")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
            print("How many moons does Earth have?")
            user=int(input("Enter your answer(1/2):"))
            if user== 1:
             print("Correct! Earth has one moon.")  
            else:
             print("Oops! You Are WRONG! Earth has only one moon.") 
     elif des==3:
        print("Are You Ready A Mission?")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
         print("Your oxygen tank is running low!")
        else:
         print("You have chosen to return to your spaceship.")
        user=int(input("Enter your answer(1/2):"))
        if user==1:
         print("1 → Search for an oxygen station nearby.")
        else:
         print("2 → Return to your spaceship") 



    case  2:
     print("You have chosen to go to Mars.") 
     des=random.randint(1, 3)
     if des==1:
      print("Fun Fact:Mars is home to the tallest volcano in the solar system, Olympus Mons.")
     elif des==2:
        print("Are You Ready For The Quiz...")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
            print("Which planet is the largest?")
            user=input("Enter your answer:")
            if user.lower()== "jupiter":
             print("Correct! Jupiter is the largest planet in our solar system.")  
            else:
             print("Oops! You Are WRONG! The largest planet is Jupiter.") 
     elif des==3:
        print("Are You Ready A Mission?")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
         print("Your Mission Question Is Here--")
         print("Your spaceship needs fuel. You have two options: 1. Search for a fuel station nearby. 2. Return to your spaceship.")
        else:
         print("You have chosen to return to your spaceship.")
        user=int(input("Enter your answer(1/2):"))
        if user==1:
         print("1 → You Chose The Correct Option! You found a fuel station and refueled your spaceship.")
        else:
         print("2 → You have chosen to return to your spaceship.") 


    case  3:     
     print("You have chosen to go to Jupiter.") 
     des=random.randint(1, 3)
     if des==1:
      print("Fun Fact:Jupiter is the largest planet in the solar system`.")
     elif des==2:
        print("Are You Ready For The Quiz...")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
            print("Jupiter is classified as a gas giant. What are the two main gases that make up most of the planet?")
            user=input("Enter your answer:")
            if user.lower()== "hydrogen and helium":
             print("Correct! Jupiter is made up of mostly hydrogen and helium.")  
            else:
             print("Oops! You Are WRONG! The two main gases that make up Jupiter are hydrogen and helium.   ") 
     elif des==3:
        print("Are You Ready A Mission?")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
         print("Your Mission Question Is Here--")
         print("Your spaceship needs fuel. You have two options: 1. Search for a fuel station nearby. 2. Return to your spaceship.")
        else:
         print("A space pirate appears!...1. Fight 2. Escape")
        user=int(input("Enter your answer(1/2):"))
        if user==1:
         print("1 → You Chose The Correct Option! You fought off the space pirate and continued your journey.")
        else:
         print("2 → You have chosen to escape from the space pirate.") 
    case  4:
     print("You have chosen to go to Saturn.")
     des=random.randint(1, 3)
     if des==1:
      print("Fun Fact:Saturn is known for its beautiful rings, which are made up of ice and rock particles.")
     elif des==2:
      print("Are You Ready For The Quiz...")
      choice=input("Enter 'yes' to start: ")
      if choice.lower() == "yes":
       print("What is the name of Saturn's largest moon?")
       user=input("Enter your answer:")
      if user.lower()== "titan":
        print("Correct! Titan is Saturn's largest moon.")  
      else:
        print("Oops! You Are WRONG! Saturn's largest moon is Titan.") 
     elif des==3:
        print("Are You Ready A Mission?")
        choice=input("Enter 'yes' to start: ")
        if choice.lower() == "yes":
         print("Your Mission Question Is Here--")
         print("Your spaceship needs fuel. You have two options: 1. Search for a fuel station nearby. 2. Return to your spaceship.")
        else:
         print("You have chosen to return to your spaceship.")
         user=int(input("Enter your answer(1/2):"))
         if user==1:
            print("1 → You Chose The Correct Option! You found a fuel station and refueled your spaceship.")
         else:
            print("2 → You have chosen to return to your spaceship.")
    case 5:
     print("Exiting the Space Adventure.")
     break
    case _:
     print("Invalid destination. Please choose again.")