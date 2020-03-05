path = '/home/max/Documents/AdventofCode2019/Puzzle3/input.txt'
input_file = open(path,'r')
inputs = input_file.read()

#need dictionaries
#Check dictionary each time to see is point is already there,
	#that's where they cross
#Goal, need distance from point 0,0

#import linecache
import csv

line1 = []
line2 = []
grid1 = {}
grid2 = {}
cross = []
cross2 = []
count1 = []
count2 = []
count3 = 0

with open('input.csv', newline='\n') as b:
	input_reader = csv.reader(b)
	line1 = next(input_reader)
	line2 = next(input_reader)

#line1 = ['R10', 'U20']
#line2 = ['U10', 'R20']

#vel is the numeric value following the directional prompt
#stx is the starting x value on the "grid", is passed from trace
#sty is the starting y value on the "grid", is passed from trace
#stx and sty are changed to keep up with each "line" on the grid in trace
#hor is boo for if x value is changing in grid key
#pos is boo for if y value is changing in grid key
def move (vel, stx, sty, hor, pos, map):
	if hor == True:
		
		if pos == True:
			end = vel + stx
			for p in range(stx,end +1):
				try:
					if map[(p,sty)] == 2:
#						cross.append(abs(0-p)+abs(0-sty))
						map[(p,sty)] = map.get((p,sty),0) + 1
					else:
						map[(p,sty)] = map.get((p,sty),0) + 1
				except KeyError:	
					map[(p,sty)] = map.get((p,sty), 0) + 1
					#if grid[(p,sty)] != 1:
						#print(p,sty)
		
		if pos == False:
			end = stx - vel
			for p in range(end,stx +1):
				try:
					if map[(p,sty)] == 2:
#						cross.append(abs(0-p)+abs(0-sty))
						map[(p,sty)] = map.get((p,sty), 0)+ 1
					else:
						map[(p,sty)] = map.get((p,sty), 0)+ 1
				except KeyError:	
					map[(p,sty)] = map.get((p,sty), 0)+ 1
					#if grid[(p,sty)] != 1:
						#print(p,sty)

	if hor == False:

		if pos == True:
			end = vel + sty
			for f in range(sty,end +1):
				try:
					if map[(stx,f)] == 2:
#						cross.append(abs(0-stx)+abs(0-f))
						map[(stx,f)] = map.get((stx,f), 0) + 1
					else:
						map[(stx,f)] = map.get((stx,f), 0) + 1
				except KeyError:	
					map[(stx,f)] = map.get((stx,f), 0)+ 1
					#if grid[(stx,f)] != 1:
						#print(stx,f)

		if pos == False:
			end = sty - vel
			for f in range(end,sty +1):
				try:
					if map[(stx,f)] == 2:
#						cross.append(abs(0-stx)+abs(0-f))
						map[(stx,f)] = map.get((stx,f), 0) + 1
					else:
						map[(stx,f)] = map.get((stx,f), 0) + 1
				except KeyError:	
					map[(stx,f)] = map.get((stx,f), 0)+ 1
					#if grid[(stx,f)] != 1:
						#print(stx,f)


def trace (line, dict):
	global cross
	global count1
	global count2
	x = 0
	y = 0
	for f in line:
		letter = f[:1]
		num = int(f[1:])

		except KeyError:
			pass
		if "R" == letter:
			move(num, x, y, True, True, dict)
			x = x + num
		elif "L" == letter:
			move(num, x, y, True, False, dict)
			x = x - num
		elif "U" == letter:
			move(num, x, y, False, True, dict)
			y = y + num
		elif "D" == letter:
			move(num, x, y, False, False, dict)
			y = y - num
		else:
			raise ValueError("Unknown direction: %s" % line[spot])


trace(line2, grid2)
trace(line1, grid1)
#print(grid)

#print(grid)
#print(cross)
#print(cross2)


#q = 0
#for line in grid1:
#	cross2.append(set(grid1).intersection(set(grid2)))
#	print(q)
#	q += 1





input_file.close()
