# This is just to gen a single mon For right now I am gonna quick and dirty copy and paste so I can use this tonight. Later I plan to put all the modules and classes in their own directory and import them from that location.

import random, sys, sqlite3, getopt
from collections import Counter
from operator import itemgetter

sys.path.insert(0, "modules/")

from monmods import GetNature
from monmods import Shiny
from monmods import RareRoll
from nature import Nature
from pokemon import Pokemon
from move import Move
from ability import Ability

ability = sys.argv[1]

xability = (ability ,)

# In order to use our move function to print out info about a move first we need to know the ID of the move.

conn = sqlite3.connect('PTA_ORAS.db')

data = conn.execute('SELECT id FROM ORAS_ability WHERE name=?' , xability)
for x in data:
	ability_id = x

print Ability(ability_id)


