import entities as e
import menu as m


player = e.Player()
monster = e.Crawler()

e.run_combat(player,monster)


def test(player,monster):
    
    if not monster.isAlive:
        print(f"The {monster.type} is already dead")
        return
    
    inCombat = True
    while inCombat:
        inCombat = e.healthCheck(player,monster)
        e.combatSequence(player,monster,'player')
        m.continue_prompt()
        
        inCombat = e.healthCheck(player,monster)
        e.combatSequence(player,monster,'monster')
        m.continue_prompt()
        
    if not player.isAlive:
        print(f"You have died")
    elif not monster.isAlive:
        print(f"You have won")
        
test(player,monster)