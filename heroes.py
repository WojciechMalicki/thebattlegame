#      _
#     | |
#     | |__   ___ _ __ ___   ___  ___
#     | '_ \ / _ \ '__/ _ \ / _ \/ __|
#     | | | |  __/ | | (_) |  __/\__ \
#     |_| |_|\___|_|  \___/ \___||___/
#
#

from random import randint as rnd

class hero():
    def __init__(self, name, health, mn_attack, mx_attack, heal=None):
        self.name = name
        self.cur_health = health
        self.max_health = health
        self.min_attack = mn_attack
        self.max_attack = mx_attack
        self.defeated = []
        self.sum_of_power = 0
        self.name_of_army = None
        self.heal = heal
       
    def is_alive(self):
        if self.cur_health > 0:
            return True
        else:
            return False

    def set_hit_point(self):
        return rnd(self.min_attack, self.max_attack) 

    def display_stat_full(self):
        res = f"{self.name} [{self.cur_health}/{self.max_health}:{self.min_attack}-{self.max_attack}]"
        if self.heal is None:
            return res
        else:
            return res[:-1] + f":{self.heal}]" 

    def display_stat(self, a):
        """a => True - this is attacker, False - this is defenders
        """
        if a:
            self.hit_point = self.set_hit_point()
            self.sum_of_power += self.hit_point
            return f"{self.name} [{self.hit_point}]"
        else:
            return f"{self.name} [{self.cur_health}]"

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
        
    def add_to_army(self, hero):
        if hero.name_of_army == None:
            self.heroes.append(hero)
            hero.name_of_army = self.name
        elif hero.name_of_army == self.name:
            print(hero.name, "already belongs to this army")
        else:
            print(hero.name, "belongs to", hero.name_of_army)

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