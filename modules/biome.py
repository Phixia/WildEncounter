import random, sys, sqlite3
from collections import Counter
from nature import Nature
from move import Move
from ability import Ability
from monmods import Shiny
from monmods import GetNature
from monmods import RareRoll
from pokemon import Pokemon

class Biome(object):
#All Biomes have the following:
#		3 .txt files with lists of pokemon for common pokemon Biome_c.txt, uncommon pokemon Biome_uc.txt, and rare pokemon Biome_r.txt
#		All biomes will be used to generate random pokemon from these three files based on a d100 roll
#		All biomes will also do a d100 roll to determine if the generated pokemon is shiny or not

	def __init__(self, name):
# create a Biome object whose name is *name*.
		self.name = name

# define function to pull a common mon from a biome
	def common(self):
		self.f = open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end common
# define function to pull uncommon mon from a biome
	def uncommon(self):
		self.f= open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end uncommon
# define function to pull a rare mon from a biome
	def rare(self):
		self.f = open('biomes/%s_c.txt' %self.name)
		self.mons = self.f.read().splitlines()
		self.mon = random.choice(self.mons)
		return self.mon
# /end rare

# This actually builds the encounter and returns the mons name
	def encounter(self):
		rareness = RareRoll()
		if rareness < 6:
			self.rare()
			return self.mon
		if rareness > 5 and rareness < 41:
			self.uncommon()
			return self.mon
		else:
			self.common()
			return self.mon
# /end encounter


