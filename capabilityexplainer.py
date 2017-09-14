# I threw this script together quick to print out a capabilities description, short and simple, it needs to move to modules and get defined as a function some day.
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

capability_name = sys.argv[1]

capability_name = (capability_name ,)

conn = sqlite3.connect('PTA_ORAS.db')
data3 = conn.execute('SELECT description FROM ORAS_capability WHERE name=?', capability_name)
for row in data3:
	capability_desc = str(row[0])
conn.close()
print capability_desc
