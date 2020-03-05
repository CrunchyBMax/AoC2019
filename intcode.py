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

#path = './input.csv'
#input_file = open(path,'r')
#inputs = input_file.read()

from collections import deque
#import pdb
#spot = 0 #spot in list

#tape = [int(i) for i in open('input.csv').read().split(",")]

#stop = 0
fouroutput = 0
spots = deque(maxlen = 5) #spots deque keeps track of spots for amp, revolves as amps are called
spots.append(0) #fills spots deque with the appropriate num of values
spots.append(0)
spots.append(0)
spots.append(0)
spots.append(0)
amp5output = deque(maxlen = None) #stores all of the outputs of Amp5
finoutput = deque(maxlen = None) #stores all outputs of the last Amp5 output upon op99 being called

def spotreset():
	spots.clear()
	spots.append(0)
	spots.append(0)
	spots.append(0)
	spots.append(0)
	spots.append(0)

def op99 (prop): 
	global stop
	global finoutput
	spotreset()
	stop = 2
	finoutput.append(amp5output.pop())
	return

def op1 (bob, place, p1mode=0, p2mode=0, p3mode=0): 
	jim = 0
	tim = 0
	val1 = int(bob[place+1]) 	
	val2 = int(bob[place+2]) 
	val3 = int(bob[place+3]) 
	if p1mode == 0:
		jim = int(bob[val1])
	if p1mode == 1:
		jim = val1
	if p2mode == 0:
		tim = int(bob[val2])
	if p2mode == 1:
		tim = val2
	if p3mode == 0:
		sumval = jim + tim
		bob[val3] = sumval
	if p3mode == 1:
		raise ValueError("unknown mode for writing instr %s" % bob[place])
	return 4

def op2 (bob, place, p1mode=0, p2mode=0, p3mode=0): 
	jim = 0
	tim = 0
	val1 = int(bob[place+1]) 	
	val2 = int(bob[place+2]) 
	val3 = int(bob[place+3]) 
	if p1mode == 0:
		jim = int(bob[val1])
	if p1mode == 1:
		jim = val1
	if p2mode == 0:
		tim = int(bob[val2])
	if p2mode == 1:
		tim = val2
	if p3mode == 0:
		sumval = jim * tim
		bob[val3] = sumval
	if p3mode == 1:
		raise ValueError("unknown mode for writing instr %s" % bob[place])
	return 4

def op3 (bob, place, prop):
	par1 = int(bob[place+1])
	bob[par1] = prop.pop()
	print("input: %i" % bob[par1])
	return 2

def op4 (bob, place, prop, isamp5):
	global stop
	global fouroutput
	global spots
	global amp5output
	par1 = int(bob[place+1])
	fouroutput = bob[par1]
	print('bob@place %i' % bob[place])
	print('place + 1 %i' % (place + 1))
	print('par1 %i' % par1)
	print('place%i' % place)
	print("output: %i" % bob[par1])
	place += 2
	spots.appendleft(place)
	if isamp5 == 'y':
		amp5output.append(fouroutput)
	print('fouroutput  %i' % fouroutput)
	stop = 1
	return 2

def op5 (bob, place, p1mode=0, p2mode=0): #DONE
	if p1mode == 1:
		val1 = bob[place+1]
	if p1mode == 0:
		val3 = bob[place+1]
		val1 = bob[val3]
	if p2mode == 1:
		val2 = bob[place+2]
	if p2mode == 0:
		val4 = bob[place+2]
		val2 = bob[val4]	
	if val1 != 0:
		return (val2 - place)
	else:
		return 3

def op6 (bob, place, p1mode=0, p2mode=0): #DONE
	if p1mode == 1:
		val1 = bob[place+1]
	if p1mode == 0:
		val3 = bob[place+1]
		val1 = bob[val3]
	if p2mode == 1:
		val2 = bob[place+2]
	if p2mode == 0:
		val4 = bob[place+2]
		val2 = bob[val4]
	if val1 == 0:
		return (val2 - place)
	else:
		return 3

def op7 (bob, place, p1mode=0, p2mode=0): #DONE
	if p1mode == 1:
		val1 = bob[place+1]
	if p1mode == 0:
		val3 = bob[place+1]
		val1 = bob[val3]
	if p2mode == 1:
		val2 = bob[place+2]
	if p2mode == 0:
		val4 = bob[place+2]
		val2 = bob[val4]
	val5 = bob[place+3]
	if val1 < val2:
		bob[val5] = 1
	else:
		bob[val5] = 0
	return 4

def op8 (bob, place, p1mode=0, p2mode=0): #DONE
	if p1mode == 1:
		val1 = bob[place+1]
	if p1mode == 0:
		val3 = bob[place+1]
		val1 = bob[val3]
	if p2mode == 1:
		val2 = bob[place+2]
	if p2mode == 0:
		val4 = bob[place+2]
		val2 = bob[val4]
	val5 = bob[place+3]
	if val1 == val2:
		bob[val5] = 1
	else:
		bob[val5] = 0
	return 4

def opexecute(tape, place, prop, isamp5, instr, md1, md2, md3):
	global spots
	if instr == 99:
		place = op99(prop) #returns 'NoneType' & causes TypeError in intcode
	elif instr == 1:
		place = op1(tape, place, md1, md2, md3)
	elif instr == 2:
		place = op2(tape, place, md1, md2, md3)
	elif instr == 3:
		place = op3(tape, place, prop)
	elif instr == 4:
		place = op4(tape, place, prop, isamp5) #'isamp5' allows op4 to put output from amp5 in addit. deque for ref later
	elif instr == 5:
		place = op5(tape, place, md1, md2)
	elif instr == 6:
		place = op6(tape, place, md1, md2)
	elif instr == 7:
		place = op7(tape, place, md1, md2)
	elif instr == 8:
		place = op8(tape, place, md1, md2)
	else:
		print(place)
		print(tape)
		print(len(tape))
		raise ValueError("unknown opcode: %s" % str(spot)+" "+str(instr))
	return place

def intcode(prop, pramset, tape, isamp5):
	global stop
	global spots
	global fouroutput
	stop = 0
	place = spots.pop()
	print("prop:")   
	print(prop)
	print("pramset:") 
	print(pramset)
	while stop == 0:
		print("value on tape[%d] spot: %i" % (place,tape[place]))
		nuts = str(tape[place])
		x = opexecute(tape, place, prop, isamp5, int((nuts[-2:] or 0)), int((nuts[-3:-2] or 0)), int((nuts[-4:-3] or 0)), int((nuts[:-4] or 0)))
		try:
			place = place + x
		except TypeError: #should only TypeError after running op99
			if stop == 2:
				break
	print('spots:')
	print(spots)
	if stop == 2:
		return 'false' #causes ValueError in Amp_ method
	else:
		return fouroutput #returns output to be append to prevoutput deque in Amp_ method

#input_file.close()
#new_inputs.close()