from teamfive.utils import clear_screen, buffer
    
def condino_menu():
    while True:
        clear_screen()
        print("Hello Everyone! I am Ciara Marie Condino")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Caya")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("7. Exit")
            
        choice = input("\nEnter your choice: ")
        
        clear_screen()
            
        match choice:
            case "1":
                print("Name: Ciara Marie Condino")
                print("Age: 21 years old")
                print("I love playing Grow a Garden in Roblox")
                buffer()
            case "2":
                print("Goal: Graduate and travel")
                buffer()
            case "3":
                print("Keep up the good work, Condino!")
                buffer()
            case "4":
                print("Keep on dreaming. Padayon!")
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