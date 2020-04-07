# -*- coding: utf-8 -*-
# 	
# 	
# 	  __ _  __ _ _ __ ___   ___
# 	 / _` |/ _` | '_ ` _ \ / _ \
# 	| (_| | (_| | | | | | |  __/
# 	 \__, |\__,_|_| |_| |_|\___|
# 	  __/ |
# 	 |___/

from heroes import *	
from fight import *

Armand = hero("Armand", 65, 25, 28)
Agamonk = hero("Agamonk", 165, 10, 26)
Azzo = hero("Azzo", 85, 40, 42, 10)
Annagab = hero("Annagab", 50, 16, 24)
Enfor = hero("Enfor", 50, 1, 32)
Forkt = hero("Forkt", 15, 1, 17)
Graom = hero("Graom", 18, 1, 15)
Gragh = hero("Gragh", 18, 1, 16)
Ghoae = hero("Ghoae", 18, 1, 19)
Frads = hero("Frads", 18, 1, 19)
Horoae = hero("Horoae", 18, 1, 28)
Gersad = hero("Gersad", 90, 1, 51)
Groar = hero("Groar", 18, 1, 24)
Roasr = hero("Roasr", 18, 1, 23)
Rarck = hero("Rarck", 18, 1, 25)
Sparek = hero("Sparek", 17, 1, 6)
Drobar = hero("Drobar", 19, 1, 11)

Light = army("Light")
Dark = army("Dark")

Light.add_to_army(Armand)
Light.add_to_army(Agamonk)
Light.add_to_army(Azzo)
Light.add_to_army(Annagab)
Light.add_to_army(Agamonk)
Dark.add_to_army(Azzo)
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
Dark.add_to_army(Sparek)
Dark.add_to_army(Drobar)


fight_game(Light, Dark)