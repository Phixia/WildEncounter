import sys, random, sqlite3
from pprint import pprint
sys.path.insert(0, "modules/")
# I tried to make a function to import the other functions, but it did not seem to work...
#from monmods import Imports
from nature import Nature
from move import Move
from monmods import Shiny
from monmods import GetNature
from monmods import RareRoll
from collections import Counter
from collections import OrderedDict
from operator import itemgetter
from ability import Ability
#I tried to make a DB function but was having issues returning the connection string...
#from monmods import DbConnect
#from monmods import OldDbConnect
#from monmods import DbQuery
#from monmods import DbClose

class Pokemon(object):
# All Pokemon have the following:
# A name (the kind of pokemon)
# 6 Stats HP, Atk, Def, SpAtk, SpDef, and Speed
# WeightClass and Size
# A list of Capabilities
# A type or 2 types
# A nature
# An Ability
# A move set
# A sex (Maybe!)

	def __init__(self, mon, level):
		self.name = mon
		self.mon = (mon,)
		self.level = int(level)
		self.shiny = Shiny()
		self.nature = GetNature()
		conn = sqlite3.connect('PTA_ORAS.db')
		data = conn.execute('SELECT id, type1, type2, hp, atk, def, satk, sdef, spd, height, weight, `capture_rate`, exp_drop FROM ORAS_pokemon WHERE name=?' , self.mon)
		for row in data:
			self.WeightClass = row[10]
			self.Size = row[9]
			self.HP = row[3]
			self.Atk = row[4]
			self.Def = row[5]
			self.SpAtk = row[6]
			self.SpDef = row[7]
			self.Speed = row[8]
			self.Type1 = row[1]
			self.Type2 = row[2]
			self.num = int(row[0])
			self.caprate = int(row[11])
			self.exp = row[12]
		conn.close()
# I am going to use the old DB for this because currently it stores it in a more sane manner;
# again I tried to use a cool function for this and it failed...
#		self.OldData()


# Gonna try to move Capabilities to using the PTA db not the PTU db. Still using Gender from the PTU db as the PTA one has % signs and I need to figure them out.
		conn = sqlite3.connect('PTA')
		olddata = conn.execute('SELECT Male, Female, Capabilities FROM Pokemon where Name=?' , self.mon)
		for row in olddata:
			self.Capabilities = row[2]
			self.Mchance = int(row[0])
			self.Fchance = int(row[1])
		conn.close()

# This is the new capabilities section 
		conn = sqlite3.connect('PTA_ORAS.db')
		data = conn.execute('SELECT stage, overland, surface, underwater, sky, burrow, jump, power, intelligence FROM ORAS_pokemon WHERE name=?', self.mon)
		for row in data:
			self.Stage = row[0]
			self.Overland = row[1]
			self.Surface = row[2]
			self.Underwater = row[3]
			self.Sky = row[4]
			self.Burrow = row[5]
			self.Jump = row[6]
			self.Power = row[7]
			self.Int = row[8]	
		data2 = conn.execute('SELECT capability_id FROM ORAS_pokemon_capabilities WHERE pokemon_id=?', (self.num,))
		for row in data2:
			self.capability_id = row[0]
		data3 = conn.execute('SELECT name, description FROM ORAS_capability WHERE id=?', (self.capability_id,))
		for row in data3:
			self.capability_name = row[0]
			self.capability_desc = str(row[1])
		conn.close()





		self.BaseStats = {"hp": int(self.HP), "atk": int(self.Atk), "def": int(self.Def), "satk": int(self.SpAtk), "sdef": int(self.SpDef), "spd": int(self.Speed)}

		LeveledStats = self.LevelUp()
		self.finalHPtotal = (LeveledStats.values()[0] * 3 + self.level)
		self.finalHP = LeveledStats.values()[0]
		self.finalAtk = LeveledStats.values()[1]
		self.finalDef = LeveledStats.values()[5]
		self.finalSpAtk = LeveledStats.values()[3]
		self.finalSpDef = LeveledStats.values()[2]
		self.finalSpeed = LeveledStats.values()[4]

		self.ability = self.Ability()

		
		conn = sqlite3.connect('PTA_ORAS.db')
		iddata = conn.execute('SELECT id from ORAS_ability WHERE name=?' , (self.ability,))
		for row in iddata:
			self.ability_id = row[0]
		conn.close()






# This is the function to print out our Pokemon Object so whatever we define here we will see when we run stuff.

	def __str__(self):
		output = ( "{}\n"
							"HP Total: {}\n"
							"{}\n"
							"{}\n"
							"Ability: {}\n"
							"	{}\n"
							"Base Stats{}\n"
							"	HP: {}\n"
							"	Atk: {}\n"
							"	Def: {}\n"
							"	SpAtk: {}\n"
							"	SpDef: {}\n"
							"	Speed: {}\n"
							"Current Stats {}\n"
							"	HP: {}\n"
							"	Atk: {}\n"
							"	Def: {}\n"
							"	SpAtk: {}\n"
							"	SpDef: {}\n"
							"	Speed: {}\n"
							"Type: {}/{}\n"
							"WeightClass: {}\n"
							"Size: {}\n"
							"Sex: {}\n"
							"Capture Rate: {}\n"
							"Exp Drop: {}\n"
							"Capabilities: {}\n"
							"	Int: {}\n"
							"	Power: {}\n"
							"	Overland: {}\n"
							"	Surface: {}\n"
							"	Underwater: {}\n"
							"	Sky: {}\n"
							"	Burrow: {}\n"
							"	Jump: {}\n"
							"	Capability Name: {}\n"
							"	{}\n" )
		return output.format(self.name,
									self.finalHPtotal,
									self.shiny,
									Nature(self.nature),
									"",
										Ability((self.ability_id,)),
									"",
									self.HP,
									self.Atk,
									self.Def,
									self.SpAtk,
									self.SpDef,
									self.Speed,
									"",
									self.finalHP,
									self.finalAtk,
									self.finalDef,
									self.finalSpAtk,
									self.finalSpDef,
									self.finalSpeed,
									self.Type1,
									self.Type2,
									self.WeightClass,
									self.Size,
									self.Sex(),
									self.caprate,
									self.exp * self.level,
									"",
									self.Int,
									self.Power,
									self.Overland,
									self.Surface,
									self.Underwater,
									self.Sky,
									self.Burrow,
									self.Jump,
									self.capability_name,
									self.capability_desc )





	def BaseStats(self):
		conn = sqlite3.connect('PTA_ORAS.db')
		
		data = conn.execute('SELECT number, type1, type2, hp, atk, def, satk, sdef, spd, height, weight, capture_rate, exp_drop FROM ORAS_pokemon WHERE name=?' , self.mon)
		conn.close()
		return data

	def OldData(self):
		conn = sqlite3.connect('PTA')
		olddata = conn.execute('SELECT Male, Female, Capabilities FROM Pokemon where Name=?' , self.mon)
		conn.close()
		return olddata

	def Sex(self):
		if self.Mchance == 0.0 and self.Fchance == 0.0:
			sex = 'N/A' 
		elif RareRoll() <= int(self.Mchance):
			sex = 'M'
		else:
			sex = 'F'
		return sex

	def Ability(self):
		conn = sqlite3.connect('PTA_ORAS.db')
		self.num = (self.num,)
		ability = conn.execute('SELECT ability_id from ORAS_pokemon_abilities WHERE pokemon_id=? AND level="basic" ORDER BY RANDOM() LIMIT 1' , self.num)
		ability = ability.fetchone()
		ability_name = conn.execute('SELECT name FROM ORAS_ability WHERE id=?' , ability)
		ability_name = ability_name.fetchall()
		for x in ability_name:
			ability_name = x[0]
		conn.close()
		return ability_name	


	def Naturalize(self):
		nature = Nature(self.nature)
		a = Counter(self.BaseStats)
		b = Counter(nature.StatUpMod)
		c = Counter(nature.StatDownMod)

		NewStats_counter = (a + b) - c
		
		NewStats = {}
		
		for key, value in NewStats_counter.items():
			NewStats[key] = value
		return NewStats	


# This function is where the magic happens and getting the magic to happen happens to be a total bitch
# Here we attempt to level a pokemon up and add a stat point for each level past level 1 it has gained.
# In PTA we must retain BaseRelation which means the Highest stat at level 1 must always remain the highest stat
# Andrew Howard provided much of the logic for this current itteration of LevelUp() we are collectively going to try to make the logic less hacky/lazy over the next few weeks.

	
#	def LevelUp(self):
#		StatPoints = self.level - 1
#		Stats = sorted(self.BaseStats.values(), reverse=True)
#		BaseStats = Stats[:]
#		Newstats = {}
	
#		for i in (0,5,1,2,3):
#			if StatPoints < 1:
#				break
#			Increment = random.randint(0,StatPoints)
#			StatPoints -= Increment
#			Stats[i] += Increment
#			Stats[4] += StatPoints
#			Stats.sort()

#			if ( len(set(Stats)) < len(set(BaseStats)) ):
#				print "Base relation tie problems"

#		StatOrder = sorted(self.BaseStats.keys())
#		for x in range(0,6):
#			Newstats[StatOrder[x]] = Stats[x]

#		return Newstats	


# Attempt at new LevelUp logic
	def LevelUp(self):
		StatPoints = self.level - 1
		BaseStats = self.Naturalize()
		Stats = sorted(BaseStats.items(), key=itemgetter(1), reverse=True)
		NewStats = dict(BaseStats)
#		def LeftLimit(x):
#			if Stats[x]
		while StatPoints >0:
			x = random.randint(0,5)
			x_name = Stats[x][0]
			y = x - 1
			z = int(Stats[x][1])
			a = int(Stats[y][1])
			if x == 0:
				NewStats[x_name] = z + 1
				Stats[x] = (x_name, z + 1)
				StatPoints -= 1
				continue
			elif ( z + 1) > a:
				continue
			else:
				NewStats[x_name] = z + 1
				Stats[x] = (x_name, z + 1)
				StatPoints -= 1
				continue
#		return NewStats
# Attempting to get a better printout of LevelUp() stats
		CurrentStats = dict(sorted(NewStats.items(), key=lambda x: x[1]))
		return CurrentStats



# This is going to use a new DB for the time being until I switch the old calls to use the new DB too (The old DB is for PTU so while most of the mon data works, the movesets and abilities are different)

	def Moves(self):
		level = (self.level,)
		conn = sqlite3.connect('PTA_ORAS.db')
#		data = conn.execute('SELECT * from ORAS_pokemon_moves INNER JOIN ORAS_move on ORAS_pokemon_moves.move_id = ORAS_move.id where ORAS_pokemon_moves.pokemon_id=?' , self.num)	
		data = conn.execute('SELECT move_id from ORAS_pokemon_moves where pokemon_id=? AND level<=?' , self.num + level)
		data = data.fetchall()
		return data
