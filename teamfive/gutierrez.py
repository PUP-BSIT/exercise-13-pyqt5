from teamfive.utils import clear_screen, buffer

def gutierrez_menu():
    while True:
        clear_screen()
        print("Hello, I am King Andrei Gutierrez")
        print("1 - Basic Information")
        print("2 - Goals")
        print("3 - Comment from Arguelles")
        print("4 - Comment from Caya")
        print("5 - Comment from Condino")
        print("6 - Comment from Cordova")
        print("7 - Exit")
        
        choice = input("\nSelect a team member: ")
        
        match choice:
            case "1":
                print("-Basic Information-")
                print("Name: King Andrei B. Gutierrez")
                print("Age: 20")
                print("Birthday: February 21, 2005")
                buffer()
            case "2":
                print("My Goal is to be successful in life and career.")
                buffer()
            case "3":
                print("Good luck on that, King! Hope you achieve your goals!")
                buffer()
            case "4":
                print("Keep on dreaming. Padayon!")
                buffer()
            case "5":
                print("May we achieve the dreams we desire.")
                buffer()
            case "6":
                print("Hello, I admire your goal.")
                buffer() 
            case "7":
                break   
            case _:
                print("Invalid choice. Please try again.")
                buffer()
            
                
                