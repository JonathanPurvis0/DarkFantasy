def main(): # The beginnging of the program
    print("Welcome to the story!\n" 
    "Please select what you want to do:\n" 
    "1. Start a new adventure\n"
    "2. About the game\n"
    "3. Quit\n")
    choice = input("Enter your choice (1 or 2): ") #Get user input

    if choice == '1': # If the user chooses to start a new adventure
        chapterOne()
    elif choice == '2': # If the user chooses to learn about the game
        print("About the Game")
    elif choice == '3': # If the user chooses to quit
        print("Thank you for visiting! Goodbye!")
    else: # If the user enters an invalid choice
        print("Invalid choice. Please try again.")
        main()

def chapterOne(): # Function to start the adventure
    print("Starting your adventure...\n")
    # Here you can add more code to continue the adventure

def chapterTwo():
    # Function for the second chapter of the adventure
    print("Chapter Two Text")

def chapterThree():
    # Function for the third chapter of the adventure
    print("Chapter Three Text")
    

main()