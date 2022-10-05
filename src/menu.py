# Menu functionality

import entities as e
import system


def continue_prompt():
    """Pauses program until user inputs something
    """

    input("Press a key to continue: ")


def menu_move(): # WIP
    """Move between rooms
    """
    system.clearConsole()
    print("Move")
    continue_prompt()
    system.clearConsole()


def menu_inv(player):
    """Displays the player's inventory

    Args:
        player (objec): player instance
    """
    system.clearConsole()
    print("You have the following items:")
    for item in player.inventory:
        print(f"   -{item.type}: {item.description}")
    continue_prompt()
    system.clearConsole()


def menu_health(player):
    """Displays the player's health

    Args:
        player (object): player instance
    """
    system.clearConsole()
    print(f"You have {player.health} health points!")
    continue_prompt()
    system.clearConsole()

def menu_victory_defeat(monster, mode):
    """Displays either a victory or defeat message

    Args:
        monster (object): monster instance
        mode (string): 'player' or 'monster'. determine message contents
    """
    if mode == 'player':
        system.clearConsole()
        print(f"You have defeated the {monster.type}!")
        continue_prompt()
        system.clearConsole()
        
    elif mode == 'monster':
        system.clearConsole()
        print(f"The {monster.type} has defeated you!")
        continue_prompt
        system.clearConsole()

def menu_attack(player, monster):
    """Initiates combat between player and monster

    Args:
        player (object): player instance
        monster (object): monster instance
    """
    system.clearConsole()
    if not monster.isAlive:
        print(f"The {monster.type} is already dead")
        return
    
    in_combat = True
    while in_combat:
        system.clearConsole()
        e.show_combat_health(player,monster)
        in_combat = e.healthCheck(player,monster)
        e.entity_combat(player,monster,'player')
        continue_prompt()
        
        system.clearConsole()
        e.show_combat_health(player,monster)
        in_combat = e.healthCheck(player,monster)
        e.entity_combat(player,monster,'monster')
        continue_prompt()    

    if not player.isAlive:
        menu_victory_defeat(monster,'monster')
    elif not monster.isAlive:
        menu_victory_defeat(monster,'player')

def menu_select_item(player):
    """Displays usable items from player inventory
    

    Args:
        player (object): player instance
    """
    system.clearConsole()
    print("What would you like to use?\n")
    index = 1
    for item in player.inventory:
        print(f"   -{index}. {item.type}")
        index += 1
    print("   -4. Go back")


def menu_use_item(player, choice):
    """Uses a player's item based on choice argument
        For use in the menu.
        Accepts player object and an int"""

    system.clearConsole()
    choice -= 1
    player.use_item(choice)
    continue_prompt()
    system.clearConsole()


