import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def buffer():
    input("\nPress enter to continue...")

def caya_menu():
    while True:
        clear()
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
                clear()
                print("----------Basic Information----------")
                print("Name: Karl Christian M. Caya")
                print("Age: 20 years old")
                print("Date of Birth: December 7, 2004")
                print("Gender: Male")
                buffer()
            case "2":
                clear()
                print("----------------------Goals----------------------")
                print("- I want to graduate with flying colors.")
                print("- Find a decent job that will support my family.")
                print("- I want to travel the world.")
                buffer()
            case "3":
                clear()
                # Comment holder for Arguelles
                buffer()  
            case "4":
                clear()
                # Comment holder for Condino
                buffer() 
            case "5":
                clear()
                # Comment holder for Cordova
                buffer()
            case "6":
                clear()
                print("Hi, King here!")
                buffer()    
            case "0":
                break
            case _:
                print("\nInvalid choice. Try again!")
                buffer()