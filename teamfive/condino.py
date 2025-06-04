import os

def pause():
    input("\nPress any key to continue...")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
                pause()
            case "2":
                print("Goal: Graduate and travel")
                pause()
            case "3":
                # Add Arguelles Comment
                pause()
            case "4":
                # Add Caya Comment
                pause()
            case "5":
                print("Hello, I admire your goal.")
                pause()
            case "6":
                # Add Gutierrez Comment
                pause()
            case "7":
                break
            case _:
                print("Invalid choice. Please try again.")