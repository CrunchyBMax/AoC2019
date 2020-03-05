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

path = '/home/max/Documents/AoC19/P5/input.csv'
input_file = open(path,'r')
inputs = input_file.read()

spot = 0 #spot in list

tape = [int(i) for i in open('input.csv').read().split(",")]

def op99 (bob): #DONE
	global tape
	global spot
	print(bob[0])
	print("end on 99 code")
	raise SystemExit

def op1 (bob, place, p1mode=0, p2mode=0, p3mode=0): #DONE
	global tape
	global spot
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
		raise ValueError("unknown mode for writing instr %s" % tape[spot])
	spot = place + 4

def op2 (bob, place, p1mode=0, p2mode=0, p3mode=0):#DONE
	global tape
	global spot
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
		raise ValueError("unknown mode for writing instr %s" % tape[spot])
	spot = place + 4

def op3 (bob, place, p1mode=0, p2mode=0, p3mode=0):
	global tape
	global spot
	print("Give input:")
	thing = input()
	print("Thanks. Plz wait...")
	par1 = int(bob[place+1])
	bob[par1] = thing
	spot = place + 2

def op4 (bob, place, p1mode=0, p2mode=0, p3mode=0):
	global tape
	global spot
	par1 = int(bob[place+1])
#	bob[par1] = par1
	print("opcode 4: %i" % bob[par1])
	spot = place + 2
#	raise SystemExit

def op5 (bob, place, p1mode=0, p2mode=0): #DONE
	global tape
	global spot
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
		spot = val2
	else:
		spot = place + 3

def op6 (bob, place, p1mode=0, p2mode=0):#DONE
	global tape
	global spot
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
		spot = val2
	else:
		spot = place + 3

def op7 (bob, place, p1mode=0, p2mode=0):#DONE
	global tape
	global spot
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
	spot = place + 4

def op8 (bob, place, p1mode=0, p2mode=0): #DONE
	global tape
	global spot
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
	spot = place + 4

def opexecute(instr, md1, md2, md3):
	global tape
	global spot
	if instr == 99:
		op99(tape)
	elif instr == 1:
		op1(tape, spot, md1, md2, md3)
	elif instr == 2:
		op2(tape, spot, md1, md2, md3)
	elif instr == 3:
		op3(tape, spot, md1, md2, md3)
	elif instr == 4:
		op4(tape, spot, md1, md2, md3)
	elif instr == 5:
		op5(tape, spot, md1, md2)
	elif instr == 6:
		op6(tape, spot, md1, md2)
	elif instr == 7:
		op7(tape, spot, md1, md2)
	elif instr == 8:
		op8(tape, spot, md1, md2)
	else:
		raise ValueError("unknown opcode: %s" % str(tape[spot])+" "+str(instr))

def rdinstr(pos1=0, pos2=0, pos3=0, pos4=0):
	global tape
	global spot
	pos1md = 0
	pos2md = 0
	pos3md = 0
	if pos1 == "1":
		pos1md = 1
	if pos2 == "1":
		pos2md = 1
	if pos3 == "1":
		pos3md = 1
	opexecute(int(pos4), pos1md, pos2md, pos3md)

def intcode(testlist):
#  ABCDE
#   1002

#	testlist[1] = noun
#	testlist[2] = verb
	global tape
	global spot
	spot = 0 #spot in list
	val1 = 0 #value one place after spot
	val2 = 0 #value two places after spot
	val3 = 0 #value three places after spot
	sumval = 0 #sum or product of val1 and val2

	while spot < len(tape):
		nuts = str(tape[spot])
		rdinstr(nuts[-3:-2], nuts[-4:-3], nuts[:-4], nuts[-2:])


intcode(tape)

#testlist = [int(i) for i in open(path).read().split(",")]

#for noun in range(100):
#	for verb in range(100):

#		testlist = [int(i) for i in open(path).read().split(",")]

#		ans = intcode(testlist, noun, verb)
#		if ans == 19690720:
#			ans =  (100 * noun) + verb
#			print("answer is: %d" % ans)
#			assert ans == 7960
#			raise SystemExit


input_file.close()
#new_inputs.close()
