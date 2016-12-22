import random, sys, sqlite3
sys.path.insert(0, "modules/")
from monmods import Fossil
from monmods import Evostone
from monmods import Legendary

var = sys.argv[1]

if var == "Fossil" or var == "fossil":
	Fossil()
	sys.exit()
if var == "Evostone" or var == "evostone":
	Evostone()
	sys.exit()
if var == "Legendary" or var == "legendary":
	Legendary()
	sys.exit()
else:
	print "Error: Please enter Fossil, Evostone, or  Legendary"

