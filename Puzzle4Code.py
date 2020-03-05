# 6 digits
# within the given range
# 2 adjacent digits are the same
# going from left to right, the number never decreases
#HOW MANY DIFFERENT PASSWORDS ARE THERE????

list1 = []
list2 = []
tier1 = []
tier2 = []
tier3 = []
tier4 = []
tier5 = []
tier6 = []
tier7 = []
maybes = []

for i in range(347312, 805915):
	list1.append(str(i))
for x in list1:
	if str('00') in x:
		list2.append(x)
	elif str('11') in x:
		list2.append(x)
	elif str('22') in x:
		list2.append(x)
	elif str('33') in x:
		list2.append(x)
	elif str('44') in x:
		list2.append(x)
	elif str('55') in x:
		list2.append(x)
	elif str('66') in x:
		list2.append(x)
	elif str('77') in x:
		list2.append(x)
	elif str('88') in x:
		list2.append(x)
	elif str('99') in x:
		list2.append(x)
for y in list2:
	if y[0:1] <= y[1:2]:
		tier1.append(y)
		if y[1:2] <= y[2:3]:
			tier2.append(y)
			if y[2:3] <= y[3:4]:
				tier3.append(y)
				if y[3:4] <= y[4:5]:
					tier4.append(y)
					if y[4:5] <= y[5:6]:
						tier5.append(y)
						#answer = y


print("Original answer: %i" % len(tier5))

def salvation (groupb): #passes any number w/three consecutive digits 
						#AND two consecutive digits that are not the 
						#same as the three consecutive ones
	poop = ["00","11","22", "33", "44", "55", "66", "77", "88", "99"]
	opoop = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
	for line in groupb:
		for oturd in opoop:
			if oturd in line:
				dump = opoop.index(oturd)
				dumpp = poop[dump]
				poop.pop(dump)
				#print(poop)
				for turd in poop:
					if turd in line:
							maybes.append(line)
				poop.insert(dump, dumpp)
				#print(poop)
	#print(poop)	


def round2 (groupa): #passes any number w/out three consecutive matching digits
	opoop = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
	for line in groupa:
		opoop = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
		for oturd in opoop:
			if oturd not in line:
				opoop.remove(oturd)#000
				for oturd in opoop:
					if oturd not in line:
						opoop.remove(oturd)#111
						for oturd in opoop:
							if oturd not in line:
								opoop.remove(oturd)#222
								for oturd in opoop:
									if oturd not in line:
										opoop.remove(oturd)#333
										for oturd in opoop:
											if oturd not in line:
												opoop.remove(oturd)#444
												for oturd in opoop:
													if oturd not in line:
														opoop.remove(oturd)#555
														for oturd in opoop:
															if oturd not in line:
																opoop.remove(oturd)#666
																for oturd in opoop:
																	if oturd not in line:
																		opoop.remove(oturd)#777
																		for oturd in opoop:
																			if oturd not in line:
																				opoop.remove(oturd)#888
																				for oturd in opoop:
																					if oturd not in line:
																						tier6.append(line)
																						
###NEED TO ADD 333 444 555 INTO LOOP IN round3

def round3 (groupc): #Only pass numbers with 1 set of 3 consecutive digits
	global tier6
	opoop = [ "333", "444", "555","666", "777", "888", "999"]
	for line in groupc:
		opoop = [ "333", "444", "555", "666", "777", "888", "999"]
		for oturd in opoop: 
			if oturd in line:
				dump = oturd
				opoop.remove(oturd)
				if any(oturd in line for oturd in opoop):
					break
				else:
						tier6.append(line)
				opoop.append(dump)
#		if opoop[0] in line:
#			if opoop[1] in line:
#				break
#				if opoop[2] in line:
#					break
#			else:
#				if opoop[2] in line:
#					break
#				else:
#					tier6.append(line)#777
#		else:
#			if opoop[1] in line:
#				if opoop[2] in line:
#					break
#				else:
#					tier6.append(line)#888
#			else:
#				if opoop[2] in line:
#					tier6.append(line)#999

def dupbrigade (withdup):
	global tier7
#	withdup = set(withdup)
	seen = set()
	for item in withdup:
		if item not in seen:
			seen.add(item)
			tier7.append(item)


#bill(tier5)
#print("maybes: %s" % maybes)
salvation(tier5)
round2(tier5)
round3(maybes)
dupbrigade(tier6)
print("num of dups: %i" % (int(len(tier6)) - int(len(tier7))))
print("after salv: %s" % tier6)
if 291 < len(tier7) < 392:
	print(len(tier7))
else:
	print("nope")
	print(len(tiery))

