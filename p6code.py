# Every object orbits exactly 1 other object
# Use sets? 
# Total number of orbits in my map(input)

path = '/home/max/Documents/AoC19/P6/input.txt'
input_file = open(path,'r')
inputs = input_file.read()

mymap = [str(i) for i in open('input.txt').read().split("\n")]
#print(mymap)
mapp = {}
planets = []
total = 0
closest = 0
comtosan = []
comtoyou = []
sharedtosan = []
sharedtoyou = []
simdump = {}
closest = 0

def planetlist(orbits, arblist, maplib):
	global mymap
	global mapp
	global planets
	for line in orbits:
		plan1 = line[:3]
		plan2 = line[4:]
		if plan1 not in arblist:
			arblist.append(plan1)
		if plan2 not in arblist:
			arblist.append(plan2)
#	for oline in arblist:
#		maplib[oline] = maplib.get(oline,1)



def mapping (orbits, arblist, maplib): #mymap, planets, mapp
	global mymap
	global mapp
	global planets
	for line in orbits: #orbitee)orbiter
		orbitee = line[:3]
		orbiter = line[4:]
		maplib[orbiter] = orbitee #dict of ea. planet's one orbitee			


def pathmake (orbits, arblist): #NOT IN USE
	global mymap #list of planets w/orbits
	global mapp #dict
	global planets #list of planets ONLY
	frontier = ()
	frontier.put(COM) #needs to read planets into dict of (orbits):orbited
	came_from = {}
	came_from[COM] = None
	while not frontier.empty(): #loops for a while
		current = frontier.get() #current square is last in frontier list
		for next in graph.planets(current): #looks at point in graph 
			if next not in came_from: #if point in graph not in came_from dict
				frontier.put(next) #put next in frontier to be called from above
				came_from[next] = current #make entry in dict next, current

def pathfind (arblist, maplib, specs, target, catch, ocatch, pathdump):
	global mymap
	global mapp
	global planets
	global total
	global simdump
	global comtosan
	global comtoyou
	global sharedtosan
	global sharedtoyou
	start = specs
	total = 0
#	for indiv in arblist:
	current = target #current square is goal
	path = [] #place to keep the edges back to the start
	while current != start: #while current square is not the start square
		path.append(current) #put the current square at the end of the path list
		current = maplib[current] #make current the value in the came from list
	if catch == True:
		for line in path:
			pathdump.append(line)
	if catch == False:
		#simdump = name of planet:len(path)
		pathdump.get(target, 1)
		pathdump[target] = len(path)
#	if ocatch == True:
#		pathdump = len(path)
	 

planetlist(mymap, planets, mapp)
mapping(mymap, planets, mapp)

pathfind(planets, mapp, 'COM', 'SAN', True, False, comtosan)
s = set(comtosan)
pathfind(planets, mapp, 'COM', 'YOU', True, False, comtoyou)
y = set(comtoyou)
for plan in s & y:
	pathfind(planets, mapp, 'COM', plan, False, False, simdump)
for plan in simdump:
	if closest < simdump[plan]:
		closest = simdump[plan]
for plan in simdump:
	if closest == simdump[plan]:
		closestplan = plan
simdump[closest] = simdump.get(closest, closestplan)
shared = simdump[closest]
print(shared)
pathfind(planets, mapp, shared, 'SAN', True, True, sharedtosan)
pathfind(planets, mapp, shared, 'YOU', True, True, sharedtoyou)
maindistance = len(sharedtosan) + len(sharedtoyou)
print('path from you to santa is %i' % maindistance)





#pathfind(planets, mapp)
#if total == 0:
#	print(mapp)
#else:	
#	print(total)

#if 1566864 > sum(mapp.values()) > 9665 and sum(mapp.values()) != 1565095 and sum(mapp.values()) != 1315998:
#	print(sum(mapp.values()))
#else:
#	print("nope %i" % sum(mapp.values()))

input_file.close()