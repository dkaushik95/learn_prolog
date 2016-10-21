print "This is the monkey banana problem"
print "There is a room containing a monkey, chair and some bananas. That have been hanged from the center of ceiling"
climb_chair = raw_input("Can the monkey climb the chair? {Y|y|N|n}")
put_chair = raw_input("Did he put the chair below the banana? {Y|y|N|n}")
if put_chair.lower() == 'y':
	if climb_chair.lower() == 'y':
		print "The monkey is smart and can climb"
	else:
		print "The monkey is smart but cannot climb"
else:
	if climb_chair.lower() == 'y':
		print "The monkey is not smart but can climb"
	else:
		print "The monkey is not smart and cannot climb"