import time
import os

def slow_print(text, delay=0.05): # Function to print text slowly. Thanks ChatGPT!
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clearScreen(): # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): # The beginnging of the program
    print("EMS Run on Halloween Gone Wrong!\n\n" 
    "Please select what you want to do:\n" 
    "1. Start a new adventure\n"
    "2. About the game\n"
    "3. Quit\n")
    choice = input("Enter your choice (1, 2 or 3): ") #Get user input
    clearScreen() # Clear the screen after input

    if choice == '1': # If the user chooses to start a new adventure
        startGame()
    elif choice == '2': # If the user chooses to learn about the game
        aboutGame()
    elif choice == '3': # If the user chooses to quit
        print("Thank you for visiting! Goodbye!")
    else: # If the user enters an invalid choice
        print("Invalid choice. Please try again.")
        main()

def aboutGame(): # Function to display information about the game
    print("This is a text-based adventure game created for CPIN267.\n" \
    "You will navigate through different chapters and make choices that affect the outcome of the story.\n"
    "There is a point system, the scoring is as follows:\n"
    "20 - 27 points: You both escape and the monster is captured.\n"
    "12 - 20 points: You sacrifice yourself for the boy.\n"
    "9 - 12 points: You both die and the monster escapes.\n"
    "Enjoy your adventure!\n")

def startGame(): # Function to start the adventure
    score = 0  # Initialize score
    clearScreen()  # Clear the screen

    slow_print("Halloween Night | EMS Station | 6:00 PM") 
    slow_print("You are Loren Logan. You've just picked up a shift for a sick coworker...")
    slow_print("Your 24-hour shift just turned into a 48-hour marathon.")
    slow_print("Michael Marshall, your boss, pats your shoulder. 'You're a lifesaver, Loren. Literally.'")

    slow_print("\n*Radio crackles to life*")
    slow_print("Dispatch: Unit 12, suspicious activity reported near Pineview Estates. Possible injury in haunted maze. Respond immediately.")
    input("\nPress Enter to continue...")

    slow_print("\nYou and your partner Will Patrick arrive on scene. A group of kids is gathered near a spooky maze entrance.")
    slow_print("A boy points at the maze. 'We were horsing around. Timmy ran into Kyle and hit his head. Kyle came out, but Timmy didn't.'")

    #First choice
    slow_print("What do you do?")
    slow_print("1. Send the other kid back in. (1 point)")
    slow_print("2. Wait for Timmy to come out. (2 points)")
    slow_print("3. Go in and find Timmy yourself. (3 points)")
    choice1 = input("Choose (1/2/3): ")

    if choice1 == '1':
        score += 1
    elif choice1 == '2':
        score += 2
    elif choice1 == '3':
        score += 3
    else:
        print("Invalid choice. Defaulting to choice 1.")
        score += 1

    if choice1 == "3":
        slow_print("\nYou grab your flashlight and enter the maze.")
        slow_print("Inside, you hear faint crying. You follow it and find... a puddle of blood. No kid.")
        slow_print("You shine your light around and notice muddy footprints leading out the back of the maze and into the woods.")

        # Second Choice
        slow_print("\nWhat do you do?")
        slow_print("1. Leave the scene. (1 point)")
        slow_print("2. Go into the forest alone. (2 points)")
        slow_print("3. Recruit people nearby to help. (3 points)")
        choice2 = input("Choose (1/2/3): ")

        if choice2 == "1":
            score += 1
        elif choice2 == "2":
            score += 2
        elif choice2 == "3":
            score += 3
        else:
            slow_print("Invalid choice. Defaulting to 1.")
            score += 1

        if choice2 == "2":
            slow_print("\nYou decide to follow the trail alone into the thick forest.")
            slow_print("The trees tower above you. The light fades. The air feels... wrong.")
            slow_print("You hear a faint voice. 'Help... me...' It’s Timmy. You follow it deeper.")
            slow_print("Suddenly, a large shadow moves across your path.")

            # Third Choice
            slow_print("\nHow do you proceed?")
            slow_print("1. Chase the shadow. (1 point)")
            slow_print("2. Run away. (2 points)")
            slow_print("3. Fight the shadow. (3 points)")
            choice3 = input("Choose (1/2/3): ")

            if choice3 == "1":
                score += 1
            elif choice3 == "2":
                score += 2
            elif choice3 == "3":
                score += 3
            else:
                slow_print("Invalid choice. Defaulting to 1.")
                score += 1

            slow_print("\nYou react, heart pounding...")
            slow_print("The shadow lunges before you can act.")
            slow_print("Darkness surrounds you.")
            slow_print("You’ve been captured.")

            slow_print("\n--- CHAPTER 1 END ---")

        elif choice2 == "3":
            slow_print("\nYou call out to Will and a few parents nearby. Together, you enter the forest.")
            slow_print("But as you reach the spot... the trail goes cold. The footprints end.")
            slow_print("You hear something... but it’s too late. A large shadow swoops through the group.")
            slow_print("You black out...")
            slow_print("\n--- CHAPTER 1 END ---")

        else:
            slow_print("\nYou hesitate and walk away.")
            slow_print("Later that night, Timmy is found... unconscious and babbling about a monster.")
            slow_print("You can’t shake the feeling you missed something important.")
            slow_print("\n--- CHAPTER 1 END ---")

    elif choice1 == "2":
        slow_print("\nYou wait by the exit... 5 minutes... 10 minutes...")
        slow_print("Nothing.")
        slow_print("You realize something's wrong and finally go in. But it’s too late.")
        slow_print("The trail has gone cold.")
        slow_print("\n--- CHAPTER 1 END ---")

    else:
        slow_print("\nYou tell the kid to go back in.")
        slow_print("He gulps and steps in... only to come running back out screaming.")
        slow_print("'S-Something grabbed me!'")
        slow_print("You realize this is no ordinary injury call.")
        slow_print("\n--- CHAPTER 1 END ---")
        
    print(f"Chapter One Score: {score}")

    

main()
