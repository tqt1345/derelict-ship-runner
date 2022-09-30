import system

def continue_prompt():
    '''Requests player input any key.
        Used to pause program until user wishes to
        continue'''
        
    input("Press a key to continue: ")

def menu_move():
    system.clearConsole()
    print("Move")
    continue_prompt()
    system.clearConsole()
    
def menu_inv(player):
    system.clearConsole()
    print("You have the following items:")
    for item in player.inventory:
        print(f"   -{item.type}: {item.description}")
    continue_prompt()
    system.clearConsole()
    
def menu_health(player):
    system.clearConsole()
    print(f"You have {player.health} health points!")
    continue_prompt()
    system.clearConsole()
