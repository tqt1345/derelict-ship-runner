# Player and enemy classes
import random
import gear
class Player:
    def __init__(self) -> None:
        self.health = 100
        self.weapon = None
        self.max_inventory = 3
        self.inventory = [gear.SmallMedKit(), gear.Grenade()]
        
    def attack(self):
        return self.weapon.get_damage()
    
    def pickup(self,item):
        if len(self.inventory) < 3:
            self.inventory.append(item)
        else:
            print("Inventory full!")
        
    def throw_grenade(self):
        pass
    def use_medkit(self):
        pass
class Enemy:
    def __init__(self) -> None:
        self.health = None
        self.min_damage = None
        self.max_damage = None
        self.type = None
        
        def attack(self):
            damage = random.randint(self.min_damage,self.max_damage)
            return damage

class Crawler(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.health = 30
        self.min_damage = 2
        self.max_damage = 4
        self.type = 'crawler'

class Impaler(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.health = 20
        self.min_damage = 6
        self.max_damage = 12
        self.type = 'impaler'
        
class FleshMound(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.health = 80
        self.min_damage = 1
        self.max_damage = 6
        self.type = 'fleshmound'

# Entity related functions

def view_inventory(player):
    if player.inventory:
        for item in player.inventory:
            i = 1
            print(f"({i}): {item.type}")
            i+=1