import system
import time

def quit_program():
    system.clearConsole()
    print("Thank you for playing!")
    time.sleep(2)
    system.clearConsole()
    quit()
    
def opening_prompt():
    system.clearConsole()
    answer = input("Would you like to play? yes/no ").lower().strip()
    if answer ==  'yes':
        return True
    else:
        return False

def game_start_msg():
    system.clearConsole()
    print("You wake up from cryostasis."
          "\nYou must reach the end of the ship to survive...")
    
def main():
    while True:
        if opening_prompt():
            game_start_msg()
            break
        else:
            quit_program()

if __name__ == "__main__":
    main()

