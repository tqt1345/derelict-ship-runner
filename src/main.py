
import system
import time
import entities

def quit_program():
    system.clearConsole()
    print("Thank you for playing!")
    time.sleep(2)
    system.clearConsole()
    quit()
    
def opening_prompt():
    system.clearConsole()
    answer = input("Would you like to play? yes/no"
                   "\n=>: ").lower().strip()
    if answer ==  'yes':
        return True
    else:
        return False

def game_start_msg():
    system.clearConsole()
    print("You wake up from cryostasis."
          "\nYou must reach the end of the ship to survive...")
    
def continue_prompt():
    input("Press a key to continue: ")
    return True
    
'''
def choice(player):
    system.clearConsole()
    prompt = ("What would you like to do?"
              "\n   -Move"
              "\n   -Action")
    
    move_prompt = (f"What would you like to do?"
          "\n   -Move forward"
          "\n   -Move right"
          "\n   -Move left"
          "\n   -Move back"
          "\n   -Use item"
          "\n   -View inventory"
          "\n=>:")
    
    choice = input(prompt).lower().strip()
    if choice == "move" or choice == "m":
        input(move_prompt)
        
    elif choice == "action" or choice == 'a':
        pass
'''

def menu():
    player = entities.Player()
    monster = None
    
    initial_prompt = ("\nWhat would you like to do?"
              "\n   -1. Move"
              "\n   -2. Action"
              "\n   -3. Quit game"
              "\n=>: ")
    action_prompt = ("What would you like to do?"
                     "\n   -1. View inventory"
                     "\n   -2. View Health"
                     "\n   -3. Use item"
                     "\n   -4. Go back"
                     "\n   -5. Quit game"
                     "\n=>: ")
    use_item_prompt = ("What would you like to use?"
                       "\n   -1.{}"
                       "\n   -2.{}"
                       "\n   -3.{}"
                       "\n   -4. Nothing, go back"
                       "\n=>: ")
    while True:
        choice = int(input(initial_prompt))
        if choice == 1: # Menu 1: Move
            system.clearConsole()
            print("Move")
            continue_prompt()
            system.clearConsole()
        elif choice == 2: # Menu 2: Action
            system.clearConsole()
            while True:
                choice = int(input(action_prompt))
                if choice == 1: # Menu 2: View inventory
                    system.clearConsole()
                    print("You have the following items:")
                    for item in player.inventory:
                        print(f"   -{item.type}: {item.description}")
                    continue_prompt()
                    system.clearConsole()
                elif choice == 2: # Menu 3: View Health
                    system.clearConsole()
                    print(f"You have {player.health} health points!")
                    continue_prompt()
                    system.clearConsole()
                elif choice == 3: # Menu 4: Use item
                    while True:
                        choice = int(input(use_item_prompt))
                        if choice == 1: # Use item 1
                            print("Use item 1")
                        elif choice == 2: # Use item 2
                            print("Use item 2")
                        elif choice == 3: # Use item 3
                            print("Use item 3")
                        elif choice == 4:# Go back
                            break
                elif choice == 4: # Menu 2: Go back
                    break
                elif choice == 5: # Menu 2: Quit
                    quit_program()
        elif choice == 3: # Menu 1: Quit
            quit_program()
                 
    
def main():
    player = entities.Player()
    while True:
        if opening_prompt():
            game_start_msg()
            menu()
        else:
            quit_program()

if __name__ == "__main__":
    main()

