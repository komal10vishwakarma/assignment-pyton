import random


def rock_paper_scissors():

    print("================================")
    print("     ROCK PAPER SCISSORS GAME")
    print("================================")

    choices = ["rock", "paper", "scissors"]

    while True:

        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "4":
            print("Thank you for playing!")
            break

        if user_choice == "1":
            user = "rock"
        elif user_choice == "2":
            user = "paper"
        elif user_choice == "3":
            user = "scissors"
        else:
            print("Invalid choice! Please try again.")
            continue

        computer = random.choice(choices)

        print("\nYou chose:", user)
        print("Computer chose:", computer)

        if user == computer:
            print("It's a Draw!")

        elif user == "rock" and computer == "scissors":
            print("You Win!")

        elif user == "paper" and computer == "rock":
            print("You Win!")

        elif user == "scissors" and computer == "paper":
            print("You Win!")

        else:
            print("Computer Wins!")

