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
        
        sleep(t)
        
        r_of_b(army2.army[a2].name, army2.name, army1.army[a1].name, army1.name,
            army2.army[a2].attack, army1.army[a1].health)
        army1.army[a1].health -= army2.army[a2].attack
        if not army1.army[a1].is_alive():
            if a1 == len(army1.army) - 1:
                print(army1.army[a1].name + " is death")
                print(army2.name + " is win")
                d_a(army2.army)
                return 0
            else:
                print(army1.army[a1].name + " is death")
                sleep(t2)
                a1 += 1
                print(army1.army[a1].display_stat() + " start fighting")
