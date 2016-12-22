## This script will attempt to build a .txt file with a list of all the moves available for each Mon sorting them by
## TM, Tutor Moves, Level up, Egg Moves
import sqlite3
import sys
#First we need a mon name

mon = sys.argv[1]
mon = (mon,)

# now we need to build out some functions which will do DB calls for each of our move sets.

def Mon_ID(mon):
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT id FROM ORAS_pokemon where name=?', mon)
	for x in data:
		mon_id = x[0]
	conn.close()
	return mon_id

def TM(mon_id):
	print "TM Move List \n"
	mon_id = (mon_id,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT tm_hm_id FROM ORAS_pokemon_tms_hms where pokemon_id=?', mon_id)
	for x in data:
		move_data = conn.execute('SELECT name FROM ORAS_move where id=?', x)
		move_data = move_data.fetchall()
		for y in move_data:
			print y[0]
	conn.close()
	return     

def Egg_Move(mon_id):
	print "\n Egg Move List \n"
	mon_id = (mon_id,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT move_id FROM ORAS_pokemon_egg_moves where pokemon_id=?', mon_id)
	for x in data:
		move_data = conn.execute('SELECT name FROM ORAS_move where id=?', x)
		move_data = move_data.fetchall()
		for y in move_data:
			print y[0]
	conn.close()
	return

def Tutor_move(mon_id):
	print "\n Tutor Move List \n"
	mon_id = (mon_id,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT move_id FROM ORAS_pokemon_tutor_moves where pokemon_id=?', mon_id)
	for x in data:
		move_data = conn.execute('SELECT name FROM ORAS_move where id=?', x)
		move_data = move_data.fetchall()
		for y in move_data:
			print y[0]
	conn.close()
	return



def Level_move(mon_id):
	print "\n Level Move List \n"
	mon_id = (mon_id,)
	conn = sqlite3.connect('PTA_ORAS.db')
	data = conn.execute('SELECT move_id, level FROM ORAS_pokemon_moves where pokemon_id=? ORDER BY level ASC', mon_id)
	for x in data:
		move_id = x[0]
		move_id = (move_id,)
		move_data = conn.execute('SELECT name FROM ORAS_move where id=?', move_id)
		level = x[1]
		for y in move_data:
			print y[0], level
	conn.close()
	return








TM(Mon_ID(mon))
Egg_Move(Mon_ID(mon))
Tutor_move(Mon_ID(mon))
Level_move(Mon_ID(mon))




