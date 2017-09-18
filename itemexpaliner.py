# This script lets you input an item class and name and tells you about it
import sys,getopt,sqlite3,random
sys.path.insert(0, "modules/")
from items import *

item_name = sys.argv[1]
item_class = sys.argv[2]

item_name = (item_name,)
# the item class is what tells us which table in the DB to search, so we need to make sure we are using one of the following; Berry, PokeBall, Curative, Xdrug, Drug, Evostone, Held, TM 

if item_class == 'Berry':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT berry_id FROM ORAS_berries where berry_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()	
	Berries(item_id)

elif item_class == 'PokeBall':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT ball_id FROM ORAS_pokeballs where ball_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	PokeBall(item_id)

elif item_class == 'Curative':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_id FROM ORAS_curatives where item_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	Curative(item_id)

elif item_class == 'Xdrug':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_id FROM ORAS_drugs where drug_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	Xdrug(item_id)

elif item_class == 'Drug':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT drug_id FROM ORAS_drugs where drug_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	Drug(item_id)

elif item_class == 'Evostone'
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_id FROM ORAS_evoitems where item_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	Evostone(item_id)


elif item_class == 'Held':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT item_id FROM ORAS_helditem where item_name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	Held(item_id)


elif item_class == 'TM':
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT id FROM ORAS_TMs_HMs where name=?', item_name)
	for row in data:
		item_id = (row[0],)
	conn.close()
	TM(item_id)


else:
	print 'ERROR, your class must be one of the following: Berry, PokeBall, Curative, Xdrug, Drug, Evostone, Held, TM'
