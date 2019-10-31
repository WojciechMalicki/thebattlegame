# 	
# 	
# 	  __ _ _ __ ___ _ __   __ _
# 	 / _` | '__/ _ \ '_ \ / _` |
# 	| (_| | | |  __/ | | | (_| |
# 	 \__,_|_|  \___|_| |_|\__,_|
# 	
# 	

from heroes import *

Armand = hero("Armand", 41, 14)
Agamonk = hero("Agamonk", 30, 14)
Azzo = hero("Azzo", 85, 18)
Annagab = hero("Annagab", 40, 18)
Enfor = hero("Enfor", 30, 7)
Forkt = hero("Forkt", 15, 9)
Graom = hero("Graom", 18, 5)
Gragh = hero("Gragh", 18, 5)
Ghoae = hero("Ghoae", 18, 5)
Frads = hero("Frads", 18, 5)
Horoae = hero("Horoae", 18, 5)
Gersad = hero("Gersad", 18, 5)
Groar = hero("Groar", 18, 20)
Roasr = hero("Roasr", 18, 20)
Rarck = hero("Rarck", 18, 20)

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
Dark.add_to_army(Groar)
Dark.add_to_army(Roasr)
Dark.add_to_army(Rarck)

print(Light.display_alive_heroes())
print(Dark.display_alive_heroes())

fight(Light, Dark)
