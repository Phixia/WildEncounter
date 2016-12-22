import random, sys, sqlite3

def Shiny():
	# Note: Shiny chance for my game is 1:100 if you want to be true to the video game it is either 1:4000 or 1:8000 (older generations)
	shinychance = random.randint(1,100)
	if shinychance == 1:
		shiny = "SHINY!"
	else:
		shiny = " "
	return shiny
# /end shiny

def RareRoll():
	rareness = random.randint(1,100)
	return rareness
# / end roll for rareness

# function to get a nature from DB
def GetNature():
	conn = sqlite3.connect('PTA_ORAS.db')
#	data = conn.execute('SELECT Name FROM Natures ORDER BY RANDOM() LIMIT 1')
#	DbConnect()
	data = conn.execute('SELECT name FROM ORAS_nature ORDER BY RANDOM() LIMIT 1')
#	DbQuery('SELECT name FROM ORAS_nature ORDER BY RANDOM() LIMIT 1')
	for row in data:
		nature = row[0]
	return nature

def Fossil():
	print(random.choice(list(open('biomes/fossil.txt'))))
	return

def Evostone():
	print(random.choice(list(open('biomes/evostone.txt'))))
	return

def Legendary():
	shiny = Shiny()
	print shiny
	print(random.choice(list(open('biomes/legendary.txt'))))
	return


#def OldDbConnect():
#	conn = sqlite3.connect('PTA')
#	return conn

#def DbConnect():
#	conn = sqlite3.connect('PTA_ORAS.db')
#	return conn

#def DbClose():
#	conn.close()
#	return

#def DbQuery(x):
#	DbConnect()
#	data = conn.execute(x)
#	DbClose()
#	return data

#def Imports():
#	import random, sys, sqlite3
#	from collections import Counter
#	from monmods import Shiny
#	from monmods import GetNature
#	from monmods import RareRoll
#	from monmods import DbConnect
#	from monmods import OldDbConnect
	#from monmods import DbClose
#	from monmods import DbQuery
#	from nature import Nature
#	from pokemon import Pokemon
#	from move import Move
		
