# Menu functionality

import system

def continue_prompt():
    '''Requests player input any key.
        Used to pause program until user wishes to
        continue'''
        
    input("Press a key to continue: ")

def menu_move():
    '''WIP
        moves the player between rooms'''
    system.clearConsole()
    print("Move")
    continue_prompt()
    system.clearConsole()
    
def menu_inv(player):
    '''Displays the player's inventory'''
    system.clearConsole()
    print("You have the following items:")
    for item in player.inventory:
        print(f"   -{item.type}: {item.description}")
    continue_prompt()
    system.clearConsole()
    
def menu_health(player):
    '''Displays the player's health'''
    system.clearConsole()
    print(f"You have {player.health} health points!")
    continue_prompt()
    system.clearConsole()

def menu_attack(player,enemy):
    '''TODO
        Initiates combat sequence between player and enemy
        Accepts player object and enemy'''
    system.clearConsole()
    print("You attack the enemy")
    continue_prompt()
    system.clearConsole()
    
def menu_select_item(player):
    '''Displays selectable items from the player's
        inventory
        Accepts player object'''
    system.clearConsole()
    print("What would you like to use?\n")
    index = 1
    for item in player.inventory:
        print(f"   -{index}. {item.type}")
        index += 1
    print("   -4. Go back")

def menu_use_item(player, choice):
    '''Uses a player's item based on choice argument
        For use in the menu.
        Accepts player object and an int'''
        
    system.clearConsole()
    choice -= 1
    player.use_item(choice)
    continue_prompt()
    system.clearConsole()


