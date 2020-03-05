#Opening Puzzle input
'/home/max/Documents/AdventofCode2019/Puzzle1/*'
path = '/home/max/Documents/AdventofCode2019/Puzzle1/input'
input_file = open(path,'r')
inputs = input_file.read()

new_inputs = open('newinputs.txt','r+')
new_inputs.write(inputs)

masses = []

with open('newinputs.txt', 'r') as newinputs:
		for line in newinputs:
			currentPlace = line[:-1]
			if int(len(masses)<100):
				masses.append(int(int(currentPlace)/3) -2)

			



allmass = sum(masses)


print(masses)
print(allmass)


#def fuelneed(num1, num2=3, num3=2):
	#return (num1/num2)- num3



#for line in inputs:
	#print(fuelneed(line))
	

input_file.close()
new_inputs.close()

