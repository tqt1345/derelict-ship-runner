# Player and enemy classes
import random
class Player:
    def __init__(self) -> None:
        self.health = 100

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