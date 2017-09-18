# This script is used to determine what a pokemon with the pickup ability picks up after a fight
import sys,getopt,sqlite3,random
sys.path.insert(0, "modules/")
from items import *

# First we need to roll 1d20 then look up the id of the item 1-20 that we rolled in our item database.
def d20Roll():
	roll = random.randint(1,20)
	return roll

# There is a table in the player handbook page 257 that shows what items you get from pickup rolls. Using that table I made a function for each item type located in modules/items.py

roll = d20Roll()
if roll >= 1 and roll <= 5:
	none()

elif roll >= 6 and roll <= 8:
	Xdrug(0)

elif roll >=9 and roll <= 10:
	Berries(0)

elif roll >=11 and roll <=12:
	PokeBall(0)

elif roll >=13 and roll <=16:
	Curative(0)

elif roll == 17:
	EvoStone(0)

elif roll == 18:
	Drug(0)

elif roll == 19:
	Held(0)

elif roll == 20:
	Tm(0)

else:
	print "ERROR"


