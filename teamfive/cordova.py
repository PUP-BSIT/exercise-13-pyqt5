from teamfive.utils import clear_screen, buffer

def cordova_menu():
    while True:
        clear_screen()
        print("\nBonjour! Je suis Aron Stephen S. Cordova")
        print("Hello! I am Aron Stephen S. Cordova")
        print("\n1. About me")
        print("2. My goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Caya")
        print("5. Comment from Condino")
        print("6. Comment from Gutierrez")
        print("7. Exit menu")

        choice = input("\nEnter your choice: ")

        clear_screen()

        match choice:
            case "1":
                print("Name: Aron Stephen S. Cordova")
                print("Age: 20 years old")
                print("Birthdate: March 3, 2005")
                buffer()
            case "2":
                print("Goal: Graduate")
                buffer()
            case "3":
                print("Goodluck on your journey, Aron! Keep up the good work!")
                buffer()
            case "4":
                print("Keep on dreaming. Padayon!")
                buffer()
            case "5":
                print("May we achieve the dreams we desire.")
                buffer()
            case "6":
                print("Hi, King here!")
                buffer()
            case "7":
                break
            case _:
                print("\nInvalid choice.")
                buffer()