# 	  __ _       _     _
# 	 / _(_)     | |   | |
# 	| |_ _  __ _| |__ | |_
# 	|  _| |/ _` | '_ \| __|
# 	| | | | (_| | | | | |_
# 	|_| |_|\__, |_| |_|\__|
# 	        __/ |
# 	       |___/

from time import sleep
from itertools import zip_longest as zip_long
from heroes import *

def fight(army1, army2):
    a1 = 0
    a2 = 0
    t = 1
    t2 = 1
    
    print(army1.heroes[a1].display_stat_full(), "vs", army2.heroes[a2].display_stat_full())        
    while 1:
        sleep(t)
        print(army1.heroes[a1].display_stat(True), "->", army2.heroes[a2].display_stat(False))
        army2.heroes[a2].cur_health -= army1.heroes[a1].hit_point
        if not army2.heroes[a2].is_alive():
            print(army2.heroes[a2].name, "is death")
            army1.heroes[a1].add_to_list_defeated(army2.heroes[a2].name)
            if a2 == len(army2.heroes) - 1:
                print(army1.name, "is win")
                print(army1.display_alive_heroes())
                army1.display_of_all_heroes_defeated()
                army2.display_of_all_heroes_defeated()
                return 0
            else:
                sleep(t2)
                a2 += 1
                print(army2.heroes[a2].display_stat_full() +  " start fighting")
        army1, army2 = army2, army1
        a1, a2 = a2, a1

def fight_game(army1, army2):
	your_turn = 0
	enemy_turn = 0
	count_turns = 1

	def arena():
		print("Turn:", count_turns)
		print("-------------")
		print("Your army:", army1.name)
		for h in army1.heroes:
			print("\t" + h.name)
		print()
		a = 1
		for h in army2.heroes:
			print("\t" + str(a) + ". " + h.name)
			a += 1

	def choose():
		pass

	arena()