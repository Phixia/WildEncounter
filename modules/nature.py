import random, sys, sqlite3, getopt
sys.path.insert(0, "modules/")
from collections import Counter
from monmods import GetNature
from monmods import Shiny
from monmods import RareRoll

class Nature(object):
	conn = sqlite3.connect('PTA_ORAS.db')
	ModUp = 2
	ModDown = 2
	def __init__(self,nature):
# I have to put strings that go into sqlite3 queries in () with a comma so we do that below;
		natname = (nature,)
		natdata = Nature.conn.execute('SELECT `raise`, lower FROM ORAS_nature where name=?' , natname)
		self.name = nature
		for row in natdata:
			self.StatUp = row[0]
			self.StatDown = row[1]
		if self.StatUp == "None":
			Nature.ModUp = 0
		if self.StatDown == "None":
			Nature.ModDown = 0		
		if self.StatUp == "hp":
			Nature.ModUp = 1
		if self.StatDown == "hp":
			Nature.ModDown = 1
		self.StatUpMod = {str(self.StatUp): int(Nature.ModUp)}
		self.StatDownMod = {str(self.StatDown): int(Nature.ModDown)}
	def __str__(self):
		return "Nature: {}\n+{} {}\n-{} {}".format(self.name, Nature.ModUp, self.StatUp, Nature.ModDown, self.StatDown)
