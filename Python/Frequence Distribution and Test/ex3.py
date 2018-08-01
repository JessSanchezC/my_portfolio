#ex3.py

# W2.D3.17	test to check the outcome of the alice_in_wonderfland, List of Lists

def freq_distribution(lttr):
	
	filename = "alice_in_wonderland.txt"
	file = open(filename, encoding="utf8")

	result = []
	counter = []
	#          01234567890123567890123456
	alphabet ='abcdefghijklmnopqrstuvwxyz'
	
	#create list of list with each letter
	for l in alphabet:
		l_l = [l,0]
		counter.append(l_l)
	
	#count letter
	for line in file: #read line		
		for letter in line: #read char in line
			if letter.isalpha():		
				for n in range (len(counter)): #count letter		
					if counter[n][0] == letter.lower():		
						counter[n][1] += 1
		
	#print(counter) # print it in a better format!! 
	# print('\n')
	# for row in counter:
	# 	print (row)
	for l in range(len(counter)):
		if counter[l][0] == lttr.lower():
			result = [lttr,counter[l][1]] 
			return result

	return result

# W2.D3.18	test to check the outcome of the alice_in_wonderfland, Dict	

def freq_distribution2(lttr):
	
	filename = "alice_in_wonderland.txt"
	file = open(filename, encoding="utf8")

	result = {}
	counter={}
	#         01234567890123567890123456
	alphabet='abcdefghijklmnopqrstuvwxyz'
	
	#create dictionaty with alphabet
	for l in alphabet:
		counter[l]=0

	# 	print(counter)
	
	#count letter
	for line in file: #read line		
		for letter in line: #read char in line
			if letter.isalpha():		
				for c in counter:
					if c == letter.lower():
						counter[c] += 1

	# 			for n in range (len(counter)): #count letter		
	# 				if counter[n][0] == letter.lower():		
	# 					counter[n][1] += 1
		
	# print(counter) # print it in a better format!!
	# for c in counter:
		# print(c+': '+str(counter[c]))
	
	result[lttr] = counter[lttr.lower()]

	return result
	 
# l='a' #
# print(freq_distribution(l))

# l='j'
# print(freq_distribution(l))

# l='z'
# print(freq_distribution(l))

# l='a' #
# print(freq_distribution2(l))

# l='j'
# print(freq_distribution2(l))

# l='z'
# print(freq_distribution2(l))