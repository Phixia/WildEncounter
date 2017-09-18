# Moving the functions from pickup.py into a module file called items.py for use with other python scripts.
import sys, sqlite3, random

def none():
	print"No item is found."
	return

def Xdrug(idroll):
	if idroll == 0:
		idroll = random.randint(1,11)
	drugID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_name, drug_effect, drug_value FROM ORAS_drugs where drug_id =?', drugID)
	for row in data:
		drug = row[0]
		drugE = row[1]
		drugV = row[2]
	print drug
	print drugE
	print drugV
	conn.close()
	return

def Berries(idroll):
	if idroll == 0:
		idroll = random.randint(1,67)
	berryID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT berry_name, berry_flavor, berry_effect, berry_value FROM ORAS_berries where berry_id =?', berryID)
	for row in data:
		berry = row[0]
		berryF = row[1]
		berryE = row[2]
		berryV = row[3]
	print berry
	print berryF
	print berryE
	print berryV
	conn.close()
	return

def PokeBall(idroll):
	if idroll == 0:
		idroll_values = list(range(1,25))	
	idroll_values.remove(4)
	ballID = random.choice(idroll_values)
	ballID = (ballID,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT ball_name, ball_modifyer, ball_effect, ball_value  FROM ORAS_pokeballs where ball_id =?', ballID)
	for row in data:
		ball = row[0]
		ballM = row[1]
		ballE = row[2]
		ballV = row[3]
	print ball
	print ballM
	print ballE
	print ballV
	conn.close()
	return

def Curative(idroll):
	if idroll == 0:
		idroll = random.randint(1,17)
	itemID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name, item_effect, item_value FROM ORAS_curatives where item_id =?', itemID)
	for row in data:
		item = row[0]
		itemE = row[1]
		itemV = row[2]
	print item
	print itemE
	print itemV
	conn.close()
	return

def EvoStone(idroll):
	if idroll == 0:
		idroll = random.randint(1,9)
	itemID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name, item_value FROM ORAS_evoitems where item_id =?', itemID)
	for row in data:
		evostone = row[0]
		evostoneV = row[1]
	print evostone
	print evostoneV
	conn.close()
	return

def Drug(idroll):
	if idroll == 0:
		idroll = random.randint(12,19)
	drugID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_name, drug_effect, drug_value FROM ORAS_drugs where drug_id =?', drugID)
	for row in data:
		drug = row[0]
		drugE = row[1]
		drugV = row[2]
	print drug
	print drugE
	print drugV
	conn.close()
	return

def Held(idroll):
	if idroll == 0:
		idroll = random.randint(1,22)
	heldID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_name, item_frequency, item_effect, item_value FROM ORAS_helditem where item_id=?', heldID)
	for row in data:
		item = row[0]
		itemF = row[1]
		itemE = row[2]
		itemV = row[3]
	print item
	print itemF
	print itemE
	print itemV
	conn.close()
	return

def Tm(idroll):
	if idroll == 0:
		idroll = random.randint(1,106)
	tmID = (idroll,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT name FROM ORAS_TMs_HMs where id=?', tmID)
	for row in data:
		name = row[0]
	print name
	conn.close()
	return