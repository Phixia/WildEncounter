import sys, sqlite3, random
sys.path.insert(0, "modules/")
#from monmods import Imports
#Imports()



class Ability(object):
	
	def __init__(self,ability_id):
		self.ability_id = ability_id
		conn = sqlite3.connect('PTA_ORAS.db')
		data = conn.execute('SELECT name, activation, `limit`, keyword, effect from ORAS_ability where id=?' , self.ability_id)
		for row in data:
			self.name = str(row[0])
			self.activate = str(row[1])
			self.limit = str(row[2])
			self.keyword = str(row[3])
			self.effect = row[4].encode('utf-8')
		return
	def __str__(self):
		output = ( "{}\n"
							"Activation: {}\n"
							"Limit: {}\n"
							"Keyword: {}\n"
							"Effect: {}\n")

		return output.format(self.name,
								self.activate,
								self.limit,
								self.keyword,
								self.effect)
