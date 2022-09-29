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
        self.type = "Small Med Kit"
        self.description = "Heals 25 health"

class MediumMedKit():
    def __init__(self) -> None:
        self.heal = 50
        self.type = "Medium Med Kit"
        self.description = "Heals 50 health"
class LargeMedKit():
    def __init__(self) -> None:
        self.heal = 75
        self.type = "Large Med Kit"
        self.description = "Heals 75 health"
class Grenade():
    def __init__(self) -> None:
        self.damage = 30
        self.type = "Grenade"
        self.description = "Deals 30 damage"



