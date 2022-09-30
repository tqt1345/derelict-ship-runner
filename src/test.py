import entities
player1 = entities.Player()

for item in player1.inventory:
    print(item.type)

print()

player1.health -= 25
print(player1.health)

player1.use_item(1)
print(player1.health)

for item in player1.inventory:
    print(item.type)