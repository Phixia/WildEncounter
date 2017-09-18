# This script is to gen a single mon when you know what mon you want to gen(not random)
import sys
from operator import itemgetter
sys.path.insert(0, "modules/")
from pokemon import Pokemon
from move import Move

# To call this program do the following from CLI python pokemon.py PokemonName(Currently Cap sensitive) Level
mon = sys.argv[1]
level = sys.argv[2]
pokemon = Pokemon(mon, level)

print pokemon

for x in pokemon.Moves():
	print "\n", Move(x)
