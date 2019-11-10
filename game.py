# 	
# 	
# 	  __ _  __ _ _ __ ___   ___
# 	 / _` |/ _` | '_ ` _ \ / _ \
# 	| (_| | (_| | | | | | |  __/
# 	 \__, |\__,_|_| |_| |_|\___|
# 	  __/ |
# 	 |___/

from heroes import *	

Azzo = hero("Azzo", 85, 40, 42, 30)
Annagab = hero("Annagab", 50, 16, 24)
Enfor = hero("Enfor", 50, 1, 32)
Forkt = hero("Forkt", 15, 1, 17)

Light = army("Light")
Dark = army("Dark")

Light.add_to_army(Azzo)
Light.add_to_army(Annagab)
Dark.add_to_army(Enfor)
Dark.add_to_army(Forkt)

fight_game(Light, Dark)