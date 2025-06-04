from teamfive.utils import clear_screen, buffer

def arguelles_menu():
    while True:
        clear_screen()
        print("Good Day! I am Norlan C. Arguelles\n")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Caya")
        print("4. Comment from Condino")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        print("")
        
        match choice:
            case "1":
                print("Name: Norlan C. Arguelles")
                print("Date of Birth: December 10, 2004")
                print("Age: 20")
                print("Talents: Singing, Drawing")
                buffer()
            case "2":
                print("To be a successful UX/UI Designer.")
                buffer()
            case "3":
                print("Keep on dreaming. Padayon!")
                buffer()
            case "4":
                print("May we achieve the dreams we desire.")
                buffer()
            case "5":
                print("Hello, I admire your goal.")
                buffer()
            case "6":
                print("Hi, King here!")
                buffer()
            case "7":
                break
            case _:
                print("Invalid choice. Please try again.")
                buffer()