# -*- coding: utf-8 -*-
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
    """
    requires:
    name: string
    health: int
    minimum attack power: int
    maximum attack power: int
    healing skill: bool (default: None) 
    """
    def __init__(self, name, health, mn_attack, mx_attack, heal=None):
        self.name = name
        self.cur_health = health
        self.max_health = health
        self.min_attack = mn_attack
        self.max_attack = mx_attack
        self.defeated = []
        self.sum_of_power = 0 # total sum of hit points given
        self.name_of_army = None # belonging to the army
        self.heal = heal
       
    def is_alive(self):
        """
        returns bool
        """
        if self.cur_health > 0:
            return True
        else:
            return False

    def set_hit_point(self):
        """
        sets the hit points
        """
        return rnd(self.min_attack, self.max_attack) 

    def display_stat_full(self):
        """
        returns full statistics
        """
        res = f"{self.name} [{self.cur_health}/{self.max_health}:{self.min_attack}-{self.max_attack}]"
        if self.heal is None:
            return res
        else:
            return res[:-1] + f":{self.heal}]" 

    def display_stat(self, turn):
        """
        displays statistics about attack or current health
        input turn: True - this is attacker, False - this is defenders
        """
        if turn:
            self.hit_point = self.set_hit_point()
            self.sum_of_power += self.hit_point
            return f"{self.name} [{self.hit_point}]"
        else:
            return f"{self.name} [{self.cur_health}]"

    def add_to_list_defeated(self, name):
        """
        adds to deafeted list by this hero
        """
        self.defeated.append(name)

    def display_of_defeated(self):
        """
        displays defeated list by this hero
        """
        defeated = self.name + " defeated "
        for d in self.defeated:
            defeated += d + " "
        return defeated.strip() + f" ({self.sum_of_power})"

class army():
    """
    requires:
    name: string
    """
    def __init__(self, name):
        self.name = name
        self.heroes = []
        
    def add_to_army(self, hero):
        """
        adds to army hero
        if hero belongs to this army or another get info
        """
        if hero.name_of_army == None:
            self.heroes.append(hero)
            hero.name_of_army = self.name
        elif hero.name_of_army == self.name:
            print(hero.name, "already belongs to this army")
        else:
            print(hero.name, "belongs to", hero.name_of_army)

    def display_alive_heroes(self):
        """
        returns current list of live heroes
        """
        me = ""
        for m in self.heroes:
            if m.is_alive():
                me += m.name + " "
        me = me.strip()
        return self.name + ": " + me

    def display_of_all_heroes_defeated(self):
        """
        call display_of_defeated for every hero belongs to this army
        """
        for h in self.heroes:
            print(h.display_of_defeated())    