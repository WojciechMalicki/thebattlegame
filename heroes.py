#      _  _ ___ ___  ___  ___ ___
#     | || | __| _ \/ _ \| __/ __|
#     | __ | _||   / (_) | _|\__ \
#     |_||_|___|_|_\\___/|___|___/
#
from time import sleep

class hero():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def display_stat(self):
        return f"{self.name} [{self.health}:{self.attack}]"
    

class army():
    def __init__(self, name):
        self.name = name
        self.heroes = []
        
    def add_to_army(self, name_hero):
        self.heroes.append(name_hero)
        
    def display_alive_members(self):
        me = ""
        for m in self.heroes:
            if m.is_alive():
                me += m.name + " "
        me = me.strip()
        return self.name + ": " + me
    

def fight(army1, army2):
    a1 = 0
    a2 = 0
    t = 0.2
    t2 = 0.5
    
    def r_of_b(n_a, n_a_a, n_d, n_a_d, p_a, d_h):
        print(n_a + "(" + n_a_a + ") hit " + n_d
            + "(" + n_a_d + ") [" + str(d_h) + "-" + str(p_a) + "=" 
            + str(d_h - p_a) + "]")
    
    print(army1.heroes[a1].display_stat(), "vs", army2.heroes[a2].display_stat())        
    while 1:
        sleep(t)
        r_of_b(army1.heroes[a1].name, army1.name, army2.heroes[a2].name, army2.name,
            army1.heroes[a1].attack, army2.heroes[a2].health)
        army2.heroes[a2].health -= army1.heroes[a1].attack
        if not army2.heroes[a2].is_alive():
            if a2 == len(army2.heroes) - 1:
                print(army2.heroes[a2].name + " is death")
                print(army1.name + " is win")
                print(army1.display_alive_members())
                return 0
            else:
                print(army2.heroes[a2].name + " is death")
                sleep(t2)
                a2 += 1
                print(army2.heroes[a2].display_stat() +  " start fighting")
        army1, army2 = army2, army1
        a1, a2 = a2, a1
