# This script is used to determine what a pokemon with the pickup ability picks up after a fight
import sys,getopt,sqlite3,random

# First we need to roll 1d20 then look up the id of the item 1-20 that we rolled in our item database.
def d20Roll():
	roll = random.randint(1,20)
	return roll


# There is a table in the player handbook page 257 that shows what items you get from pickup rolls. Using that table we are going to make a function for each type of item to randomly pull an item of that type from our DB.

def none():
	print"No item is found."
	return

def Xdrug():
	idroll = random.randint(1,11)
	drugID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_name FROM ORAS_drugs where drug_id =?', drugID)
	for row in data:
		drug = row[0]
	print drug
	conn.close()
	return

def Berries():
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT berry_name FROM ORAS_berries ORDER BY RANDOM() LIMIT 1')
	for row in data:
		berry = row[0]
	print berry
	conn.close()
	return

def PokeBall():
	idroll_values = list(range(1,25))
	idroll_values.remove(4)
	ballID = random.choice(idroll_values)
	ballID = (ballID,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT ball_name FROM ORAS_pokeballs where ball_id =?', ballID)
	for row in data:
		ball = row[0]
	print ball
	conn.close()
	return

def Curative():
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name FROM ORAS_curatives ORDER BY RANDOM() LIMIT 1')
	for row in data:
		item = row[0]
	print item
	conn.close()
	return

def EvoStone():
	idroll = random.randint(1,9)
	itemID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name FROM ORAS_evoitems where item_id =?', itemID)
	for row in data:
		evostone = row[0]
	print evostone
	conn.close()
	return

def Drug():
	idroll = random.randint(12,19)
	drugID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_name FROM ORAS_drugs where drug_id =?', drugID)
	for row in data:
		drug = row[0]
	print drug
	conn.close()
	return

def Held():
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name FROM ORAS_helditem ORDER BY RANDOM() LIMIT 1')
	for row in data:
		item = row[0]
	print item
	conn.close()
	return

def Tm():
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT name FROM ORAS_TMs_HMs ORDER BY RANDOM() LIMIT 1')
	for row in data:
		name = row[0]
	print name
	conn.close()
	return

roll = d20Roll()
if roll >= 1 and roll <= 5:
	none()

elif roll >= 6 and roll <= 8:
	Xdrug()

elif roll >=9 and roll <= 10:
	Berries()

elif roll >=11 and roll <=12:
	PokeBall()

elif roll >=13 and roll <=16:
	Curative()

elif roll == 17:
	EvoStone()

elif roll == 18:
	Drug()

elif roll == 19:
	Held()

elif roll == 20:
	Tm()

else:
	print "ERROR"


