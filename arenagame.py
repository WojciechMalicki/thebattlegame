
import heroes

Armand = heroes.hero("Armand", 31, 5)
Agamonk = heroes.hero("Agamonk", 30, 3)
Azzo = heroes.hero("Azzo", 30, 2)
Annagab = heroes.hero("Annagab", 18, 8)
Enfor = heroes.hero("Enfor", 10, 7)
Forkt = heroes.hero("Forkt", 8, 5)
Graom = heroes.hero("Graom", 8, 5)
Gragh = heroes.hero("Gragh", 8, 5)
Ghoae = heroes.hero("Ghoae", 8, 5)
Frads = heroes.hero("Frads", 8, 5)
Horoae = heroes.hero("Horoae", 8, 5)
Gersad = heroes.hero("Gersad", 8, 5)
Roar = heroes.hero("Roar", 8, 5)

Light = heroes.army("Light")
Dark = heroes.army("Dark")

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


print(Light.display_alive_members())
print(Dark.display_alive_members())

heroes.fight(Light, Dark)
