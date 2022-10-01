# Main program file. 

import system
import time
import entities
import menu

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
            menu.menu_move()
            
        elif choice == 2: # Menu 1: Action
            system.clearConsole()
            while True: # Menu 2
                choice = int(input(action_prompt))
                if choice == 1: # Menu 2: View inventory
                    menu.menu_inv(player)
                    
                elif choice == 2: # Menu 2: View Health
                    menu.menu_health(player)
                    
                elif choice == 3: # Menu 2: Use item
                    while True: # Menu 3
                        menu.menu_select_item(player)
                        choice = int(input("=>: "))
                        if choice == 4: # Go back if 4
                            break
                        else: # Use item if not 4
                            menu.menu_use_item(player,choice)
                            break

                elif choice == 4: # Menu 2: Attack
                    menu.menu_attack(player)
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
