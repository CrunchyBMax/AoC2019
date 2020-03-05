#Opening Puzzle input
'/home/max/Documents/AdventofCode2019/Puzzle1/*'
path = '/home/max/Documents/AdventofCode2019/Puzzle1/input'
input_file = open(path,'r')
inputs = input_file.read()

new_inputs = open('newinputs.txt','r+')
new_inputs.write(inputs)

masses = []
amasses = []

with open('newinputs.txt', 'r') as newinputs:
		for line in newinputs:
			currentPlace = line[:-1]
			if int(len(masses)<100):
				calc = 0
				calc = int(int(currentPlace)/3) -2
				masses.append(calc)
				while calc > 0:
					calc = int(calc/3) -2
					if calc > 0:
						amasses.append(calc)


			



allmass = sum(masses)
parttwo = sum(amasses)
total = allmass + parttwo


print(masses)
print(amasses)
print(allmass)
print(parttwo)
print("Total " + str(total))


#def fuelneed(num1, num2=3, num3=2):
	#return (num1/num2)- num3



#for line in inputs:
	#print(fuelneed(line))
	

input_file.close()
new_inputs.close()

