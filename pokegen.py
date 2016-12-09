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

print sorted(pokemon.LevelUp().items(), key=itemgetter(1), reverse=True)


# For now I am disabling moves, the db seems to only list TMs/HMs/eggmoves/move_tutor moves for a mon... not naturally learned moves...
#for x in pokemon.Moves():
#	print Move(x)

