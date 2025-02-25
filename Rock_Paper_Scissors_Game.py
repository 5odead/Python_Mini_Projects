import random

print("#########################################")
print("#         Rock/Paper/Scissor Game       #")
print("#########################################\n")

def game():
    name = input("Enter Name: ")
    options = {1: "Rock", 2: "Paper", 3: "Scissor"}	
    while True:
        try:
            # User input
            User = int(input("Choose: 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if User not in [1, 2, 3]:
                print("Invalid Option. Please choose 1, 2, or 3.")
                continue
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        # Computer choice
        Computer = random.randint(1, 3)
        print("\nYou chose: " + options[User])
        print("Computer chose: " + options[Computer])
        
        # Determine the winner
        if User == Computer:
            print("Draw")
        elif (User == 1 and Computer == 3) or (User == 2 and Computer == 1) or (User == 3 and Computer == 2):
            print(name + " Won")
        else:
            print(name + " Lost")
        
        # Ask for rematch
        restart = input("\nRematch? (yes/no): ").lower()
        if restart != "yes":
            break

# Start the game
game()

