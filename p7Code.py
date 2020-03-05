#Comma seperated file, look at position 0
#Position 0 is either 1, 2, or 99
#Old computer understands parameter mode "0"
#OPCODE SUPERLIST:
#99 == program is finished and should stop
#1 == add two numbers together and store the third
#2 == same as 1 except multiply
#3 == takes one number and saves it to the position given by the parameter
#4 == outputs the value of its parameter
#PARAMETER MODES:
#0 == Puzzle 2; "position mode" if par. = 50 then value is stored at pos. 50
#1 == Puzzle 5; "value mode" if par. = 50 then value is 50
#New directions:
# - 1002: 2 is multiplication, then right to left, 0, 1, 0 

path = './input.csv'
input_file = open(path,'r')
inputs = input_file.read()

from collections import deque
from itertools import permutations
from itertools import combinations
import pdb

spot = 0 #spot in list

#tape1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5] #Example 1
#tape1 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10] #Example 2

tape1 = [int(i) for i in open('input.csv').read().split(",")]
tape2 = [int(i) for i in open('input.csv').read().split(",")]
tape3 = [int(i) for i in open('input.csv').read().split(",")]
tape4 = [int(i) for i in open('input.csv').read().split(",")]
tape5 = [int(i) for i in open('input.csv').read().split(",")]

prevoutput = deque(maxlen = 2)
prevoutput.append(0)
pramset = deque(maxlen = None)
stop = 0
spot = 0


from intcode import intcode
from intcode import finoutput
from intcode import fouroutput
from intcode import amp5output

def resettape():
	global tape1
	global tape2
	global tape3
	global tape4
	global tape5
	tape1 = [int(i) for i in open('input.csv').read().split(",")]
	tape2 = [int(i) for i in open('input.csv').read().split(",")]
	tape3 = [int(i) for i in open('input.csv').read().split(",")]
	tape4 = [int(i) for i in open('input.csv').read().split(",")]
	tape5 = [int(i) for i in open('input.csv').read().split(",")]#resets all amp tapes to original input

def cycle(deck): #same as peek, except with appendleft
	x = deck.pop()
	deck.appendleft(x)
	return x

def peek(deck): #returns value on right of deck
	x = deck.pop()
	deck.append(x)
	return x

def loaddeck (combo, pramset): #loads pramset deque with the parameter code for each amp
	pramset.clear()
	pramset.appendleft(int(combo[0]))
	pramset.appendleft(int(combo[1]))
	pramset.appendleft(int(combo[2]))
	pramset.appendleft(int(combo[3]))
	pramset.appendleft(int(combo[4]))

def Amp1 (prop, pramset, tape):
	if len(pramset) != 0:
		prop.append(pramset.pop())
	if len(prop) == 1:
		prop.append(prop[-1])
	try:
		prop.append(int(intcode(prop, pramset, tape, 'n'))) 
	except ValueError:
		return 'break'

def Amp2 (prop, pramset, tape):
	if len(pramset) != 0:
		prop.append(pramset.pop())
	if len(prop) == 1:
		prop.append(prop[-1])
	try:
		prop.append(int(intcode(prop, pramset, tape, 'n'))) 
	except ValueError:
		return 'break'

def Amp3 (prop, pramset, tape):
	if len(pramset) != 0:
		prop.append(pramset.pop())
	if len(prop) == 1:
		prop.append(prop[-1])
	try:
		prop.append(int(intcode(prop, pramset, tape, 'n'))) 
	except ValueError:
		return 'break'

def Amp4 (prop, pramset, tape):
	if len(pramset) != 0:
		prop.append(pramset.pop())
	if len(prop) == 1:
		prop.append(prop[-1])
	try:
		prop.append(int(intcode(prop, pramset, tape, 'n'))) 
	except ValueError:
		return 'break'

def Amp5 (prop, pramset, tape):
	global fouroutput
	isamp5 = 'y'
	if len(pramset) != 0:
		prop.append(pramset.pop())
	if len(prop) == 1:
		prop.append(prop[-1]) 
	try:
		prop.append(int(intcode(prop, pramset, tape, isamp5)))
	except ValueError:
		return 'break'

def amplist(prop, pramset, tape1, tape2, tape3, tape4, tape5): #runs amps in order until break on op99
	for x in range(10000):
		for y in range(10000):
			if	Amp1(prop, pramset, tape1) == 'break':
				break
			if	Amp2(prop, pramset, tape2) == 'break':
				break
			if	Amp3(prop, pramset, tape3) == 'break':
				break
			if 	Amp4(prop, pramset, tape4) == 'break':
				break
			if	Amp5(prop, pramset, tape5) == 'break':
				break
		else:
			continue
		break

allcombos = list(permutations('56789',5))
#allcombos = ['97856']
for line in allcombos:
	loaddeck(line, pramset) #load pramset with values of parameter set
	amplist(prevoutput, pramset, tape1, tape2, tape3, tape4, tape5) #pass in all necessary values and runs intcode till break on op99
	prevoutput.clear() #clears all prev. outputs for next run
	pramset.clear() #clear pramset just in case it's not empty already
	resettape() #resets all amp tapes
	print("*****LINE: %s*****" % str(line)) #prints out check for finishing each line in allcombos

if max(finoutput) == 31074828 or max(finoutput) == 31054404: #check if output varies from outputs already guessed
	print('Nope %i' % max(finoutput))
	print(finoutput)
	print(max(amp5output))
else:
	print('Yes! %i' % max(finoutput))

#print(finoutput)
#print(amp5output)


input_file.close()
#new_inputs.close()