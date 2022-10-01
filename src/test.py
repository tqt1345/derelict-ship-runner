import entities
num  = 1


player = entities.Player()

player.use_item(3)


for i in player.inventory:
    print(i.type)