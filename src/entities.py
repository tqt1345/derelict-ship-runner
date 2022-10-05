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

    def pickup(self, item):
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
                pass  # TODO
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
        damage = random.randint(self.min_damage, self.max_damage)
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
            i += 1


def entity_combat(player, monster, mode):
    if mode == 'player':
        dmg = player.attack()
        monster.health -= dmg
        print(f"You have dealt {dmg} to the {monster.type}!")
    elif mode == 'monster':
        dmg = monster.attack()
        player.health -= dmg
        print(f"The {monster.type} has dealt {dmg} to you!")

def end_combat(player, monster):
    pass


def healthCheck(player, monster):
    status = True

    if monster.health <= 0:
        monster.isAlive = False
        status = False
    elif player.health <= 0:
        player.isAlive = False
        status = False

    return status

def show_combat_health(player,monster):
    print(f"Your health: {player.health}")
    print(f"Enemy health: {monster.health}\n")

