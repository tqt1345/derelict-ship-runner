# classes for items

import random
# Weapon classes for player
class Weapon:
    def __init__(self) -> None:
        pass
    
    def get_damage(self):
        damage = random.randint(self.min_damage,self.max_damage)
        return damage

class Pistol(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.min_damage = 1
        self.max_damage = 2

class Rifle(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.min_damage = 4
        self.max_damage = 6

class Shotgun(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.min_damage = 1
        self.max_damage = 8

# Consumable items
class SmallMedKit():
    def __init__(self) -> None:
        self.heal = 25

class MediumMedKit():
    def __init__(self) -> None:
        self.heal = 50
class LargeMedKit():
    def __init__(self) -> None:
        self.heal = 75

class Grenade():
    def __init__(self) -> None:
        self.damage = 30

consumables = {'SmallMedKit': 25, 'MediumMedKit': 50, 'LargeMedKit': 75, 'Grenade': 30}