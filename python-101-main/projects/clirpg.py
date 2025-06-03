# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

def intro():
    print("Welcome, brave traveler")
    name = input("What is your Name? ")
    print(f"\nGreetings, {name}! You find yourself in a mysterious dungeon with two doors before you.")
    main_room(has_sword=False)

def main_room(has_sword):
    print("\nYou are in the main room. There are two doors in front of you:")
    print("1. Left Door")
    print("2. Right Door")

    choice = input("Which door do you choose? (left/right): ").strip().lower()
    
    if choice == "left":
        empty_room(has_sword)
    elif choice == "right":
        dragon_room(has_sword)
    else:
        print("Invalid choice. Try again.")
        main_room(has_sword)

def empty_room(has_sword):
    print("\nYou enter a seemingly empty room.")
    while True:
        print("\nOptions:")
        print("1. Look around")
        print("2. Go back")

        choice = input("What do you do? (look/back): ").strip().lower()

        if choice == "look":
            if not has_sword:
                print("\nYou look around and find a gleaming sword lying on the ground!")
                take = input("Do you take the sword? (yes/no): ").strip().lower()
                if take == "yes":
                    print("You have taken the sword.")
                    has_sword = True
                else:
                    print("You leave the sword where it is.")
            else:
                print("There's nothing else to find here.")
        elif choice == "back":
            main_room(has_sword)
            break
        else:
            print("Invalid choice. Try again.")

def dragon_room(has_sword):
    print("\nYou step into the room and are faced with a fearsome dragon!")
    while True:
        print("\nOptions:")
        print("1. Fight the dragon")
        print("2. Go back")

        choice = input("What do you do? (fight/back): ").strip().lower()

        if choice == "fight":
            if has_sword:
                print("\nWith your mighty sword, you slay the dragon! You win!")
            else:
                print("\nYou try to fight the dragon with your bare hands... and get eaten. Game Over.")
            break
        elif choice == "back":
            main_room(has_sword)
            break
        else:
            print("Invalid choice. Try again.")

# Start the game
intro()