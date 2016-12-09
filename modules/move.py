import sys, sqlite3, random
sys.path.insert(0, "modules/")
#from monmods import Imports
#Imports()



class Move(object):
	
	def __init__(self,move_id):
		self.move_id = move_id
		conn = sqlite3.connect('PTA_ORAS.db')
		data = conn.execute('SELECT name, type, rate, accuracy, range, stat, damage, effect1, contest from ORAS_move where id=?' , self.move_id)
		for row in data:
			self.name = str(row[0])
			self.mtype = str(row[1])
			self.rate = str(row[2])
			self.accuracy = str(row[3])
			self.mrange = str(row[4])
			self.stat = str(row[5])
			self.damage = str(row[6])
			self.effect1 = str(row[7])
			self.contest = str(row[8])	
		effect_data = conn.execute('SELECT effect2 from ORAS_move where id=?' , self.move_id)
		effect_data2 = effect_data.fetchone()
		if effect_data2 == "NULL":
			self.effect2 = "No effect"
		else:	
			for i in effect_data2:
				self.effect2 = i.encode('utf-8')
#		self.effect2 = (row[8]).encode('utf-8')
		return
	def __str__(self):
		output = ( "{}\n"
							"Type: {}\n"
							"Rate: {}\n"
							"Accuracy: {}\n"
							"Range: {}\n"
							"Stat: {}\n"
							"DamageRoll: {}\n"
							"Effect: {}\n"
							"Effect: {}\n"
							"Contest: {}\n" ) 
		return output.format(self.name,
								self.mtype,
								self.rate,
								self.accuracy,
								self.mrange,
								self.stat,
								self.damage,
								self.effect1,
								self.effect2,
								self.contest )
