from teamfive.utils import clear_screen, buffer

def caya_menu():
    while True:
        clear_screen()
        print("----------Welcome to Caya's Menu----------")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Comment from Arguelles")
        print("4. Comment from Condino")
        print("5. Comment from Cordova")
        print("6. Comment from Gutierrez")
        print("0. Exit")
        
        choice = input("\nPlease enter your choice: ")
        
        match choice:
            case "1":
                clear_screen()
                print("----------Basic Information----------")
                print("Name: Karl Christian M. Caya")
                print("Age: 20 years old")
                print("Date of Birth: December 7, 2004")
                print("Gender: Male")
                buffer()
            case "2":
                clear_screen()
                print("----------------------Goals----------------------")
                print("- I want to graduate with flying colors.")
                print("- Find a decent job that will support my family.")
                print("- I want to travel the world.")
                buffer()
            case "3":
                clear_screen()
                print("Goodluck on your journey, Caya!")
                buffer()  
            case "4":
                clear_screen()
                print("May we achieve the dreams we desire.")
                buffer() 
            case "5":
                clear_screen()
                print("Hello, I admire your goal.")
                buffer()
            case "6":
                clear_screen()
                print("Hi, King here!")
                buffer()    
            case "0":
                break
            case _:
                print("\nInvalid choice. Try again!")
                buffer()