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
count1 = 0
count2 = 0
countcount = [0]
list2 = []

with open('input.csv', newline='\n') as b:
	input_reader = csv.reader(b)
	line1 = next(input_reader)
	line2 = next(input_reader)

#vel is the numeric value following the directional prompt
#stx is the starting x value on the "grid", is passed from trace
#sty is the starting y value on the "grid", is passed from trace
#stx and sty are changed to keep up with each "line" on the grid in trace
#hor is boo for if x value is changing in grid key
#pos is boo for if y value is changing in grid key
def move (vel, stx, sty, hor, pos, map, count):
	global count1
	global count2
	global countcount
	if hor == True:
		if pos == True:
			end = vel + stx
			for p in range(stx,end +1):
				countcount.append(count)
				count += 1
				map[(p,sty)] = map.get((p,sty),0) + countcount[int(-1)]
				
		if pos == False:
			end = stx - vel
			for p in reversed(range(end, stx +1)):
				countcount.append(count)
				count += 1
				map[(p,sty)] = map.get((p,sty), 0)+ countcount[int(-1)]

	if hor == False:
		if pos == True:
			end = vel + sty
			for f in range(sty,end +1):	
				countcount.append(count)
				count += 1
				map[(stx,f)] = map.get((stx,f), 0)+ countcount[int(-1)]

		if pos == False:
			end = sty - vel
			for f in reversed(range(end, sty +1)):
				countcount.append(count)
				count += 1
				map[(stx,f)] = map.get((stx,f), 0)+ countcount[int(-1)]

def trace (line, dict, c):
	global cross
	global count1
	global count2
	global countcount
	x = 0
	y = 0
	for f in line:
		letter = f[:1]
		num = int(f[1:])
		c = countcount[int(-1)]
		if "R" == letter:
			move(num, x, y, True, True, dict, c)
			x = x + num

		elif "L" == letter:
			move(num, x, y, True, False, dict, c)
			x = x - num

		elif "U" == letter:
			move(num, x, y, False, True, dict, c)
			y = y + num

		elif "D" == letter:
			move(num, x, y, False, False, dict, c)
			y = y - num

		else:
			raise ValueError("Unknown direction: %s" % line[spot])
	countcount = [0]

trace(line1, grid1, count1)
trace(line2, grid2, count2)

cross = set(grid1)&set(grid2)
print(cross)
for elem in cross:
	print(grid1[elem], grid2[elem])
	cross2.append(grid1[elem] + grid2[elem])
cross2.pop(10)
print(min(cross2))
#print(grid1)







input_file.close()
