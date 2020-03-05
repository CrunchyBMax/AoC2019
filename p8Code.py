#Num 1s multiplied by Num 2s on layer w/ fewest 0s
#Pic fills in left to right, then move down
#first digit is the top left pixel of first layer
#last digit is the bottom right pixel of last layer
#my image is 25 pixels wide and 6 pixels tall
#'0' is black
#'1' is white
#'2' is transparent

path = './input.txt'
input_file = open(path,'r')
inputs = input_file.read()

picture = [int(i) for i in open('input.txt').read()]

layers = {}
bigzero = 150
onesandtwos = []
print(len(picture))
layerlist = []
#for i in range(int(len(picture) / 150)):
#	int(i)
#	start = (i-1)*150
#	stop = i*150
#	while start != stop:
#		layerlist.append(picture[start])
#		start += 1
#	layers[(i)] = str(layerlist)
#	layers[(i, 2)] = layers.get((i, 2), layerlist.count(2))
#	layers[(i, 0)] = 150 - (int(layers[i, 1]) + int(layers[i, 2]))
#	layerlist = []

picnum = 0
picvalue = 2
val1 = 0
y = 0
for x in range(1,101):
	xa = x
	x = []
	while len(x) <150:
		try:
			x.append(picture[y])
			y += 1
		except IndexError:
			break
	layers[xa] = x

pixelvalue = {}
#for n in range(1,151):
#		pixelvalue[n] = pixelvalue.get(n, 2)


holdlist = []
holdlist2 = []
layercount = 1
while layercount <= 100:
	hold = layers[layercount]
	for f in hold:
		holdlist.append(f)
#	for tup in holdlist:
#		try:
#			holdlist2.append(int(tup[0]))
#		except ValueError:
#			pass
#	print(holdlist2)
#	print(holdlist2[0])
	keynum = 0
	while keynum < 150:
		try:
			if pixelvalue[keynum] not in [0, 1]:
				pixelvalue[keynum] = holdlist[keynum]
		except KeyError:
			pixelvalue[keynum] = pixelvalue.get(keynum, holdlist[keynum])
		keynum = keynum +1	
	
	holdlist = []
	holdlist2 = []
	layercount += 1

print(pixelvalue)
lineone = []
linetwo = []
linethree = []
linefour = []
linefive = []
linesix = []
line = 0
while line <= 149:
	if 0 <= line <= 24:
		lineone.append(pixelvalue[line])
	elif 24 < line <= 49:
		linetwo.append(pixelvalue[line])
	elif 49 < line <= 74:
		linethree.append(pixelvalue[line])
	elif 74 < line <= 99:
		linefour.append(pixelvalue[line])
	elif 99 < line <= 124:
		linefive.append(pixelvalue[line])
	elif 124 < line <= 149:
		linesix.append(pixelvalue[line])
	line += 1
print(lineone)
print(linetwo)
print(linethree)
print(linefour)
print(linefive)
print(linesix)

#print(layers)

#print(layers)
#print(onesandtwos)




input_file.close()