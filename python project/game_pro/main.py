from digital_watch.digital import application_run
from image_slideshow.image import image_application
from rent_calculator.rent import rent_application
from student_grade_managment.student import student_applicataion
from rock_paper.rock import rock_paper_scissors
from spell_checker.spell import spell_checker


def main():

    while True:

        print("+======================================+")
        print("        PYTHON APPLICATION MENU")
        print("+======================================+")

        print("1. Digital Watch")
        print("2. Image Slideshow")
        print("3. Rent Calculator")
        print("4. Student Grade Management")
        print("5. Rock Paper Scissors")
        print("6. Spell Checker")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            application_run()

        elif choice == "2":
            image_application()

        elif choice == "3":
            rent_application()

        elif choice == "4":
            student_applicataion()

        elif choice == "5":
            rock_paper_scissors()

        elif choice == "6":
            spell_checker()

        elif choice == "7":
            print("\nThank you for using the application!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
