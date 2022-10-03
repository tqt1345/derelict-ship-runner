# classes for items

import random
import entities


# Weapon classes for player
class Weapon:
    '''Weapon class exists to be inherited from
        Contains methods for weapon usage'''

    def __init__(self) -> None:
        pass

    def get_damage(self):
        '''Returns weapons damag to be used by a player instance'''
        damage = random.randint(self.min_damage, self.max_damage)
        return damage


class Pistol(Weapon):
    '''A pistol
        Default weapon, low damage'''

    def __init__(self) -> None:
        '''Make pistol'''
        super().__init__()
        self.min_damage = 1
        self.max_damage = 2


class Rifle(Weapon):
    '''A rifle
        High damage'''

    def __init__(self) -> None:
        '''Make rifle'''
        super().__init__()
        self.min_damage = 4
        self.max_damage = 6


class Shotgun(Weapon):
    '''A shotgun
        Inconsistent damage'''

    def __init__(self) -> None:
        '''Make shotgun'''
        super().__init__()
        self.min_damage = 1
        self.max_damage = 10


# Consumable items
class SmallMedKit():
    '''A small medkit. Heals 25'''

    def __init__(self) -> None:
        '''Make small medkit'''
        self.heal = 25
        self.type = "medkit"
        self.name = "Small Med Kit"
        self.description = "Heals 25 health"


class MediumMedKit():
    '''A medium medkit. Heals 50'''

    def __init__(self) -> None:
        '''Make medium medkit'''
        self.heal = 50
        self.type = "medkit"
        self.name = "Medium Med Kit"
        self.description = "Heals 50 health"


class LargeMedKit():
    '''A large medkit. Heals 75'''

    def __init__(self) -> None:
        '''Made large medkit'''
        self.heal = 75
        self.type = 'medkit'
        self.name = "Large Med Kit"
        self.description = "Heals 75 health"


class Grenade():
    '''A grenade. Deals 30 damage'''

    def __init__(self) -> None:
        '''Make grenade'''
        self.damage = 30
        self.type = "grenade"
        self.name = "Grenade"
        self.description = "Deals 30 damage"
