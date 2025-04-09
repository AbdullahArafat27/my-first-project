from random import randint

# List of possible items the player can find
room_items = ["bow", "armour", "boomerang", "shield", "sword"]

def treasure_room():
    """Prints a message when the player finds the ultimate treasure."""
    print("You have found the ultimate treasure chest! You win the game!")
    play_again()

def item_room():
    """Simulates the player finding an item in a room."""
    item_index = randint(0, len(room_items) - 1)
    item = room_items[item_index]
    print(f"You found {item}, you decide to pick it up!")

def monster_room():
    """Handles the scenario when the player encounters a monster."""
    print("You have entered a room with a monster!")
    while True:
        choice = input("Do you choose to fight or flee? ")
        if choice == "fight":
            if fight_monster():
                return True  # Player wins and goes back to the starting room
            else:
                return False  # Game over if the player loses
        elif choice == "flee":
            print("You fled back to the starting room.")
            return True  # Player flees and goes back to the starting room
        else:
            print("Invalid choice. Please choose to fight or flee.")

def fight_monster():
    """Simulates fighting the monster. The player wins or loses based on random chance."""
    print("You are fighting the monster...")
    if randint(0, 9) > 3:
        print("You defeated the monster! You win!")
        return True 
    else:
        print("The monster defeated you. You lose the game.")
        return False

def starting_room():
    """Handles the starting room where the player chooses a door."""
    num_doors = 3
    treasure_door = randint(1, num_doors)
    print(f"You are in a room with {num_doors} doors.")
    while True:
        try:
            choice = int(input(f"Which door (1 - {num_doors}) do you choose? "))
            if choice == treasure_door:
                treasure_room()
                break
            elif 1 <= choice <= num_doors:
                encounter = randint(0, 1)
                if encounter == 0:
                    item_room()
                else:
                    if not monster_room():
                        break  # End game if the player is defeated by the monster
            else:
                print("Invalid door choice. Please choose a valid door.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_again():
    """Asks the player if they want to play again."""
    choice = input("Do you want to play again? (yes/no) ")
    if choice.lower() == "yes":
        starting_room()  # Restart the game if the player chooses 'yes'
    else:
        print("Thanks for playing!")  # End the game if the player chooses 'no'

starting_room()  # Start the game