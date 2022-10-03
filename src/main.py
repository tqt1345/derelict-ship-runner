# Main program file. 

import support as s


def main():
    """Runs the program"""
    while True:
        if s.opening_prompt():  # If user wants to play the game ->
            s.start_game()  # -> Then Play the game
        else:
            s.quit_program()


# start program
if __name__ == "__main__":
    main()
