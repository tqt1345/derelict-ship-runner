
import system
import time
import entities

def quit_program():
    '''Clears the console and displays a thank you message
    briefly before quitting.'''
    system.clearConsole()
    print("Thank you for playing!")
    time.sleep(2)
    system.clearConsole()
    quit()
    
def opening_prompt():
    '''Requests the user to start or quit the program'''
    system.clearConsole()
    answer = input("Would you like to play? yes/no"
                   "\n=>: ").lower().strip()
    if answer ==  'yes':
        return True
    else:
        return False


def continue_prompt():
    '''Requests player input any key.
        Used to pause program until user wishes to
        continue'''
        
    input("Press a key to continue: ")

def game_start_msg():
    '''Message displayed on game start'''
    system.clearConsole()
    print("You wake up from cryostasis."
          "\nYou must reach the end of the ship to survive...")

    
def start_game():
    '''Runs the game'''
    player = entities.Player() # Player instance
    monster = None # Monster instance
    
    # Input prompts
    initial_prompt = ("\nWhat would you like to do?"
              "\n   -1. Move"
              "\n   -2. Action"
              "\n   -3. Quit game"
              "\n=>: ")
    action_prompt = ("What would you like to do?"
                     "\n   -1. View inventory"
                     "\n   -2. View Health"
                     "\n   -3. Use item"
                     "\n   -4. Attack"
                     "\n   -5. Go back"
                     "\n   -6. Quit game"
                     "\n=>: ")
    use_item_prompt = ("What would you like to use?"
                       "\n   -1.{}"
                       "\n   -2.{}"
                       "\n   -3.{}"
                       "\n   -4. Nothing, go back"
                       "\n=>: ")
    
    game_start_msg()
    
    # Interactive program menu
    while True: # Menu 1
        choice = int(input(initial_prompt)) 
        if choice == 1: # Menu 1: Move
            system.clearConsole()
            print("Move")
            continue_prompt()
            system.clearConsole()
            
        elif choice == 2: # Menu 1: Action
            system.clearConsole()
            while True: # Menu 2
                choice = int(input(action_prompt))
                if choice == 1: # Menu 2: View inventory
                    system.clearConsole()
                    print("You have the following items:")
                    for item in player.inventory:
                        print(f"   -{item.type}: {item.description}")
                    continue_prompt()
                    system.clearConsole()
                    
                elif choice == 2: # Menu 2: View Health
                    system.clearConsole()
                    print(f"You have {player.health} health points!")
                    continue_prompt()
                    system.clearConsole()
                    
                elif choice == 3: # Menu 2: Use item
                    while True: # Menu 3
                        choice = int(input(use_item_prompt))
                        if choice == 1: # Menu 3: Use item 1
                            print("Use item 1")
                        elif choice == 2: # Menu 3: Use item 2
                            print("Use item 2")
                        elif choice == 3: # Menu 3: Use item 3
                            print("Use item 3")
                        elif choice == 4:# Menu 3: Go back
                            break
                        
                elif choice == 4: # Menu 2: Attack
                    system.clearConsole()
                    print("You attack the enemy")
                    continue_prompt()
                    system.clearConsole()
                elif choice == 5: # Menu 2: Go back
                    break
                elif choice == 6: # Menu 2: Quit
                    quit_program()
                    
        elif choice == 3: # Menu 1: Quit
            quit_program()
                 
    
def main():
    '''Runs the program'''
    while True:
        if opening_prompt(): # If user wants to play the game ->
            start_game() # -> Then Play the game
        else:
            quit_program()
            
# start program
if __name__ == "__main__":
    main()
