# Player and enemy classes and related functions

import random
import gear
class Player:
    '''The player'''
    def __init__(self) -> None:
        '''Make player'''
        self.health = 100
        self.weapon = None
        self.max_inventory = 3
        self.inventory = [gear.SmallMedKit(), gear.Grenade()]
        self.in_combat = False
        self.isAlive = True 
        self.weapon = gear.Pistol()
        
    def attack(self):
        '''Deal damage based on equipped weapon'''
        return self.weapon.get_damage()
    
    def pickup(self,item):
        '''Pickup an item and place it in
            the player's inventory if not full'''
        if len(self.inventory) < 3:
            self.inventory.append(item)
        else:
            print("Inventory full!")
        
    def use_item(self, index):
        '''Use a player item'''
        if self.inventory[index].type == "medkit":
            if self.health == 100:
                print("No need to heal,"
                      " you are at max health!")
            else:
                self.health += self.inventory[index].heal
                del self.inventory[index]
                if self.health < 100:
                    self.health = 100      
        elif self.inventory[index].type == "grenade":
            if self.in_combat:
                pass # TODO
            else:
                print("You aren't in combat.")

class Enemy:
    '''Enemy class exists to be inherited from'''
    def __init__(self) -> None:
        self.health = None
        self.min_damage = None
        self.max_damage = None
        self.type = None
        
    def attack(self):
        '''Returns enemy damage'''
        damage = random.randint(self.min_damage,self.max_damage)
        return damage

class Crawler(Enemy):
    '''Crawler enemy'''
    def __init__(self) -> None:
        '''Creates crawler'''
        super().__init__()
        self.health = 30
        self.min_damage = 2
        self.max_damage = 4
        self.type = 'crawler'
        self.isAlive = True

class Impaler(Enemy):
    '''Impaler enemy'''
    def __init__(self) -> None:
        '''Creates Impaler'''
        super().__init__()
        self.health = 20
        self.min_damage = 6
        self.max_damage = 12
        self.type = 'impaler'
        self.isAlive = True
        
class FleshMound(Enemy):
    '''Flesh Mound enemy'''
    def __init__(self) -> None:
        '''Creates Flesh Mound'''
        super().__init__()
        self.health = 80
        self.min_damage = 1
        self.max_damage = 6
        self.type = 'fleshmound'
        self.isAlive = True

# Entity related functions

def view_inventory(player):
    if player.inventory:
        for item in player.inventory:
            i = 1
            print(f"({i}): {item.type}")
            i+=1

def combatSequence(player,monster,mode):
    if mode == 'player':
        dmg = player.attack()
        monster.health -= dmg
        print(f"You have dealt {dmg} to the {monster.type}!")
    elif mode == 'monster':
        dmg = monster.attack()
        player.health -= dmg
        print(f"The {monster.type} has dealt {dmg} to you!")
    
def run_combat(player,monster):
    if not monster.isAlive:
        print(f"The {monster.type} is already dead")
        return
    
    inCombat = True
    while inCombat:
        inCombat = healthCheck(player,monster)
        combatSequence(player,monster,'player')
        inCombat = healthCheck(player,monster)
        combatSequence(player,monster,'monster')
        inCombat = healthCheck(player,monster)
    
    if not player.isAlive:
        print(f"You have died")
    elif not monster.isAlive:
        print(f"You have won")

def end_combat(player,monster):
    pass

def healthCheck(player,monster):
    status = True
    
    if monster.health <= 0:
        monster.isAlive = False
        status = False
    elif player.health <=0:
        player.isAlive = False
        status = False
        
    return status

        
        
        
        
'''
Combat sequence
    -loop over combat until either player or monster is dead
    -if none are at 0 health below, combat is initiated
    -Player and monster take turns dealing damage
    -after each turn, a check is done to see health
    -if the check returns 0 health, combat is ended
    -depending on who wins, final message is displayed.
    
    -needs to check who won # happens after while loop. exectues after loop is broken
    -after loop, do if else that checks health of entities
    -if monster at 0 health, print player wins, vice versa
    -if both at 0, print both dead, end game
    
while active = True
    active = check health() # if player or monster 0 health, break loop
    player attacks monster
    active = check health()
    monster attacks player
    
    
def check_health()
    dead = False
    if health = 0
        dead = True
    return dead

def endCombatMsg():
    print end combat msg

        
while True
    if check_health:
        break
    else
        player attacks monster
        

'''