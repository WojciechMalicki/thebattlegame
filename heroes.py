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
        self.army = []
        
    def add_to_army(self, name_hero):
        self.army.append(name_hero)
        
    def display_members(self):
        me = ""
        for m in self.army:
            me += m.name + " "
        me = me.strip()
        return self.name + ": " + me
    

def fight(army1, army2):
    a1 = 0
    a2 = 0
    t = 0.6
    t2 = 1
    
    def r_of_b(n_a, n_a_a, n_d, n_a_d, p_a, d_h):
        print(n_a + "(" + n_a_a + ") hit " + n_d
            + "(" + n_a_d + ") [" + str(d_h) + "-" + str(p_a) + "=" 
            + str(d_h - p_a) + "]")
            
    def d_a(a):
        print("still live: ", end='')
        for e in a:
            if e.is_alive():
                print(e.name, '',  end='')
    
    print(army1.army[a1].display_stat(), "vs", army2.army[a2].display_stat())        
    while 1:
        sleep(t)
        r_of_b(army1.army[a1].name, army1.name, army2.army[a2].name, army2.name,
            army1.army[a1].attack, army2.army[a2].health)
        army2.army[a2].health -= army1.army[a1].attack
        if not army2.army[a2].is_alive():
            if a2 == len(army2.army) - 1:
                print(army2.army[a2].name + " is death")
                print(army1.name + " is win")
                d_a(army1.army)
                return 0
            else:
                print(army2.army[a2].name + " is death")
                sleep(t2)
                a2 += 1
                print(army2.army[a2].display_stat() +  " start fighting")
        army1, army2 = army2, army1
        a1, a2 = a2, a1
