#This script is to help determine what combat stage buffs and debuffs actually mean. The combat stage mechanic slows down gameplay usually as players or GM have to sit and calculate what the outcome of changed stages really mean.

#Combat stages  can be risen or lowered  to +6 or -6. This means we have a -6 to +6 scale that starts at 0. If a stat is raised you get +25% rounded down. If it is lowered you get a -12.5% rounded up. Speed acts differently for each combat stage your speed cabailities increase by 1 or decrease by 1. You can't go lower than 1. So this script will not be used with speed stat.

import sys,getopt

# we just pass the stat value in as argv[1]
#stat = float(input("Stat value: "))
stat = float(sys.argv[1])


# Combat stage will be argv[2]
stage = float(sys.argv[2])

# now we are going to make a pair of functions to math the stat value based on the combat stage value

def cbup(stat, stage):
	percent = stage * .25
	gain = stat * percent
	final = stat + gain
	print final
	return

def cbdown(stat, stage):
	percent = stage * .125
	loss = stat * percent
	final = stat + loss
	print final
	return

# First lets make sure we have actual numbers and that the stages fall within 1 to 6 or -1 to -6


try:
	val = int(stage)
except ValueError:
	print "Stage is not a valid number"

try:
	val = int(stat)
except ValueError:
	print "Stat is not a number!?"


if stage == 0:
	print "if stage is 0 why run this script?!"

elif 1 <= stage <= 6:
	cbup(stat, stage)

elif -6 <= stage <= -1:
	cbdown(stat, stage)

else:
	print "Stage is not between -6 and 6"
 
