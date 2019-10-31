
from heroes import *

Armand = hero("Armand", 31, 8)
Agamonk = hero("Agamonk", 30, 8)
Azzo = hero("Azzo", 30, 2)
Annagab = hero("Annagab", 18, 8)
Enfor = hero("Enfor", 10, 7)
Forkt = hero("Forkt", 8, 9)
Graom = hero("Graom", 8, 5)
Gragh = hero("Gragh", 8, 5)
Ghoae = hero("Ghoae", 8, 5)
Frads = hero("Frads", 8, 5)
Horoae = hero("Horoae", 8, 5)
Gersad = hero("Gersad", 8, 5)
Roar = hero("Roar", 8, 20)

Light = army("Light")
Dark = army("Dark")

Light.add_to_army(Armand)
Light.add_to_army(Agamonk)
Light.add_to_army(Azzo)
Light.add_to_army(Annagab)
Dark.add_to_army(Enfor)
Dark.add_to_army(Forkt)
Dark.add_to_army(Graom)
Dark.add_to_army(Gragh)
Dark.add_to_army(Ghoae)
Dark.add_to_army(Frads)
Dark.add_to_army(Horoae)
Dark.add_to_army(Gersad)
Dark.add_to_army(Roar)


print(Light.display_alive_heroes())
print(Dark.display_alive_heroes())

fight(Light, Dark)
