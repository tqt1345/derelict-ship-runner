import entities as e
import menu as m
import system as s

player = e.Player()
monster = e.Crawler()

#e.run_combat(player,monster)


def test(player,monster):
    s.clearConsole()
    e.combatSequence(player,monster,'player')
    m.continue_prompt()

    s.clearConsole()
    e.combatSequence(player,monster,'monster')
    m.continue_prompt()
    
test(player,monster)