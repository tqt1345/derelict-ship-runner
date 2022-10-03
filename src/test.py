import entities as e
import menu as m


player = e.Player()
monster = e.Crawler()

e.run_combat(player,monster)


def test(player,monster):
    
    inCombat = True

    while inCombat:
        if not monster.isAlive:
            print(f"The {monster.type} is already dead")
            return
        
        inCombat = e.healthCheck(player,monster)
        e.combatSequence(player,monster,'player')
        m.continue_prompt()
        
        
        e.combatSequence(player,monster,'monster')
        m.continue_prompt()
        