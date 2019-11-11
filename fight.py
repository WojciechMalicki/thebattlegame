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
    def arena():
        a = 1
        e = len(army1.heroes) + 1
        print("\t" + army1.name + "\t\t\t\t" + army2.name)
        for n1, n2 in zip_long(army1.heroes, army2.heroes):
            if type(n1) == hero:
                stat1 = str(a) + ". " + n1.display_stat_full()
                a += 1
            else:
                stat1 = ""
            if type(n2) == hero:
                stat2 = str(e) + ". " + n2.display_stat_full()
                e += 1
            else:
                stat2 = ""
            print("\t" + stat1 + "\t\t\t\t" + stat2)

    def choose():
        pass

    arena()