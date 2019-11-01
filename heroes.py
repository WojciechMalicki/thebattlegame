#      _
#     | |
#     | |__   ___ _ __ ___   ___  ___
#     | '_ \ / _ \ '__/ _ \ / _ \/ __|
#     | | | |  __/ | | (_) |  __/\__ \
#     |_| |_|\___|_|  \___/ \___||___/
#
#

#TODO properties in class hero with information about name of army
from time import sleep
from random import randint as rnd

class hero():
    def __init__(self, name, health, mn_attack, mx_attack):
        self.name = name
        self.health = health
        self.min_attack = mn_attack
        self.max_attack = mx_attack
        self.defeated = []
        self.sum_of_power = 0
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def set_hit_point(self):
        return rnd(self.min_attack, self.max_attack) 

    def display_stat_full(self):
        return f"{self.name} [{self.health}:{self.min_attack}-{self.max_attack}]"

    def display_stat(self, a):
        if a:
            self.hit_point = self.set_hit_point()
            self.sum_of_power += self.hit_point
            return f"{self.name} [{self.hit_point}]"
        else:
            return f"{self.name} [{self.health}]"

    def add_to_list_defeated(self, name):
        self.defeated.append(name)

    def display_of_defeated(self):
        defeated = self.name + " defeated "
        for d in self.defeated:
            defeated += d + " "
        return defeated.strip() + f" ({self.sum_of_power})"


    

class army():
    def __init__(self, name):
        self.name = name
        self.heroes = []
        
    def add_to_army(self, name_hero):
        self.heroes.append(name_hero)
        
    def display_alive_heroes(self):
        me = ""
        for m in self.heroes:
            if m.is_alive():
                me += m.name + " "
        me = me.strip()
        return self.name + ": " + me

    def display_of_all_heroes_defeated(self):
        for h in self.heroes:
            print(h.display_of_defeated())
    

def fight(army1, army2):
    a1 = 0
    a2 = 0
    t = 0.5
    t2 = 1
    

    print(army1.heroes[a1].display_stat_full(), "vs", army2.heroes[a2].display_stat_full())        
    while 1:
        sleep(t)
        print(army1.heroes[a1].display_stat(True), "->", army2.heroes[a2].display_stat(False))
        army2.heroes[a2].health -= army1.heroes[a1].hit_point
        if not army2.heroes[a2].is_alive():
            print(army2.heroes[a2].name + " is death")
            army1.heroes[a1].add_to_list_defeated(army2.heroes[a2].name)
            if a2 == len(army2.heroes) - 1:
                print(army1.name + " is win")
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
