# This script is to gen a single mon when you don't know what mon you want to gen(random)
import sys, sqlite3
from operator import itemgetter
sys.path.insert(0, "modules/")
from pokemon import Pokemon
from move import Move
# To call this program do the following from CLI python randomencounter.py Level
level = sys.argv[1]

def GetMon():
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT name from ORAS_pokemon ORDER BY RANDOM() LIMIT 1')
	for i in data:
		mon = i[0]
	return mon

mon = GetMon()

pokemon = Pokemon(mon, level)

print pokemon
print sorted(pokemon.LevelUp().items(), key=itemgetter(1), reverse=True)

# For now I am disabling moves, the db seems to only list TMs/HMs/eggmoves/move_tutor moves for a mon... not naturally learned moves...
for x in pokemon.Moves():
	print "\n", Move(x)
