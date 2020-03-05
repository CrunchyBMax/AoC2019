#Comma seperated file, look at position 0
#Position 0 is either 1, 2, or 99
#99 == program is finished and should stop
#1 == add two numbers together and store the third
#2 == same as 1 except multiply
#

path = '/home/max/Documents/AdventofCode2019/Puzzle2/p2input.txt'
input_file = open(path,'r')
inputs = input_file.read()

spot = 0 #spot in list

#import csv
#with open('newinputs.csv', 'r+') as csvfile:
#	readcsv = csv.reader(csvfile, delimiter = ',')
#	for row in readcsv:
#		while spot < len(row):
#			thing = row[0+int(spot)]
#			testlist.append(int(thing))
#			spot = spot + 1
testlist = [int(i) for i in open('newinputs.csv').read().split(",")]

print(testlist)

def intcode(testlist, noun=12, verb=2):
	testlist[1] = noun
	testlist[2] = verb

	spot = 0 #spot in list
	val1 = 0 #value one place after spot
	val2 = 0 #value two places after spot
	val3 = 0 #value three places after spot
	sumval = 0 #sum or product of val1 and val2

#with open('newinputs.txt', 'r') as newinputs:
#		for line in newinputs:
#			currentPlace = line[:-1]
#			testlist.append(currentPlace)


	while spot < len(testlist):
		if testlist[spot] == 99:
			return testlist[0]

		elif testlist[spot] == 1:
			val1 = int(testlist[spot+1]) #val1 = 9
			val2 = int(testlist[spot+2]) #val2 = 10
			val3 = int(testlist[spot+3]) #val3 = 3
			sumval = int(testlist[val1]) + int(testlist[val2]) #sumval = 30 + 40
			testlist[val3] = sumval #insert 70 in position 3
			spot = spot + 4
		elif testlist[spot] == 2:
			val1 = int(testlist[spot+1]) #val1 = 3
			val2 = int(testlist[spot+2]) #val2 = 11
			val3 = int(testlist[spot+3]) #val3 = 0
			sumval = int(testlist[val1]) * int(testlist[val2]) #sumval = 70 * 50
			testlist[val3] = sumval
			spot = spot + 4

		else:
			raise ValueError("unknown opcode: %s" % testlist[spot])

part1 = intcode(testlist)
assert part1 == 4690667

testlist = [int(i) for i in open(path).read().split(",")]

for noun in range(100):
	for verb in range(100):

		testlist = [int(i) for i in open(path).read().split(",")]

		ans = intcode(testlist, noun, verb)
		if ans == 19690720:
			ans =  (100 * noun) + verb
			print("answer is: %d" % ans)
			assert ans == 7960
			raise SystemExit

#print('val1 is ' +str(val1))
#print('val2 is ' +str(val2))
#print('val3 is ' +str(val3))
#print('testlist is ' + str(len(testlist)))
#print('spot is ' + str(spot))

#print(testlist)



input_file.close()
#new_inputs.close()