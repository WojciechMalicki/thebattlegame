#      _
#     | |
#     | |__   ___ _ __ ___   ___  ___
#     | '_ \ / _ \ '__/ _ \ / _ \/ __|
#     | | | |  __/ | | (_) |  __/\__ \
#     |_| |_|\___|_|  \___/ \___||___/
#
#
from time import sleep

class hero():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.defeated = []
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def display_stat(self):
        return f"{self.name} [{self.health}:{self.attack}]"

    def add_to_list_defeated(self, name):
        self.defeated.append(name)

    def display_of_defeated(self):
        defeated = self.name + ": "
        for d in self.defeated:
            defeated += d + " "
        return defeated.strip()
    

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
    t = 0.2
    t2 = 0.5
    
    print(army1.heroes[a1].display_stat(), "vs", army2.heroes[a2].display_stat())        
    while 1:
        sleep(t)
        print(army1.heroes[a1].display_stat(), "->", army2.heroes[a2].display_stat())
        army2.heroes[a2].health -= army1.heroes[a1].attack
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
                print(army2.heroes[a2].display_stat() +  " start fighting")
        army1, army2 = army2, army1
        a1, a2 = a2, a1
