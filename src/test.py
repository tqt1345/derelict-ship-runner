import entities
player1 = entities.Player()




list = [1,2,3]

#print(player1.inventory[0].type)


print("What would you like to use?\n")
index = 1
for item in player1.inventory:
    print(f"   -{index}. {item.type}")
    index += 1