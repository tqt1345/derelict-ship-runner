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

def menu_attack(player):
    system.clearConsole()
    print("You attack the enemy")
    continue_prompt()
    system.clearConsole()
    
def menu_select_item(player):
    system.clearConsole()
    print("What would you like to use?\n")
    
    index = 1
    for item in player.inventory:
        print(f"   -{index}. {item.type}")
        index += 1
    print("   -4. Go back")

def menu_use_item(player, choice):
    system.clearConsole()
    choice -= 1
    player.use_item(choice)
    continue_prompt()
    system.clearConsole()
'''
while true
    print(what items would you like to use)
    request input

    if input = corresponding num
        item.use()
        break
    
    if item.use failed
        return to menu
        (This will be handled by the item instance
            methods. if item use fails, program will move 
            to break and return to the menu anyway)

####

item.use function

medkit:
if player.health == 100
    print(You are at max hp)
else
    player.health += heal value
    if player.health < 100
        player.health = 100


grenade:
    if player in combat:
        grenade.use()
    else:
        print(You are not in combat!)
'''