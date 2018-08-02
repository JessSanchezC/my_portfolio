#soc-wk2-cert-Jessica-Sanchez.py

print("\nWeek 2.")

#WK2_D1
print("\nDay 1:\n")

#W2.D1.01 Frequency Distribution: Alice in Wonderland
	# Calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in alice_in_wonderland.txt 
	# (fancy word for counting stuff is "frequency distribution" - because you are counting the frequency of something)
	# Store the results in a list of lists:
	# result = [  
	#             ["a", 34560], 
	#             ["b", 5027], 
	#             ... 
	#             ["z", 893]
	#          ]
	#Hint: use python's lower() method to turn all alphabetic letters into small case and count them (so "A" counts towards "a").
	#Hint: Ignore non-alphabetic numbers, you can check with python isalpha() method.

def freq_distribution():
	
	filename = "alice_in_wonderland.txt"
	file = open(filename, encoding="utf8")

	counter=[]
	#         01234567890123567890123456
	alphabet='abcdefghijklmnopqrstuvwxyz'
	
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
	print('\n')
	for row in counter:
		print (row)

	return counter

print("W2.D1.01: Frequency Distribution.\n\tAlice in Wonderland: This program count how many times each letter from'A' to 'Z' appears in  file Alice in Wonderland.txt")
input('\n>Press Enter to display the result.')
freq_distribution()
input('\n>Press Enter to go to next exercise')

print("\nW2.D1.02	Test: Python the Hard Way,  5 exercises (Optional)")
print("Completed on separate file, please run test_ex")

input('\n>Press Enter to go to next exercise')

# #WK2_D2
print("\nDay 2:\n")
# #W2.D2.03 chr()
# 	#There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
print('W2.D2.04 chr(): Print A-Z and a-z, from ASCII, correct the code to print all the alphabet (Hint, we only want A-Z and a-z)')
input('\n>Press Enter to display the result.')
for i in range(65,65+2*32):#fixed the range
	if chr(i).isalpha():#print only alpha char
		print(i, " stands for ", chr(i))

input('\n>Press Enter to go to next exercise')

#2.D2.05 Make a function that prints A-Z and a-z

def print_chr():
	
	for i in range(65,65+2*32):
		if chr(i).isalpha():
			print(i, " stands for ", chr(i))

print('W2.D2.05 chr(): Make a function that prints A-Z and a-z.')
input('\n>Press Enter to display the result.')
print_chr()
input('\n>Press Enter to go to next exercise')

#W2.D2.06 Cypher
# #Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
def cypher():
	
	message = input('\nType a message and it will be turned into numbers: ')
	c_message=[]
	##alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
	abc_dict={}

	#buid dictionary with a:char
	for i in range(65,65+2*32):#fixed the range
		if chr(i).isalpha():#print only alpha char
			abc_dict[chr(i)]=i
	#print(abc_dict)

	for letter in message:
		#print(letter)
		if letter.isalpha():
			c_message.append(abc_dict[letter]) 
		else:
			c_message.append(letter)

	print(c_message)

print('\nW2.D2.06: It\'s a cypher.')
cypher()
input('\n>Press Enter to go to next exercise')

#W2.D2.07 ceaser cypher
	#Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.

def ceasarify():
	print('\nThis program shift the letter from your message by the number given.')
	
	message = ''
	while message == '':
		message=(input ('Please write a message: ')).lower()
	print (message)

	n = ''
	while n == '':
		n=int (input ('Please enter a number: '))
	
	#           01234567890123456789012345
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	ceasarified = ''

	
	for letter in message:
		if letter.isalpha():
			i = alphabet.index(letter)
			i += n
			
			if i >= len(alphabet): #to ensure that index is in range
				while i >= len(alphabet):
					i -= len(alphabet)
			
			if i < len(alphabet) *- 1: #to ensure that index is in range
				while i < len(alphabet) *- 1:
					i += len(alphabet)


			ceasarified+=alphabet[i]
		else: 
			ceasarified+=letter
		# print(ceasarified)

	
	print('Your ceasarified message is: "'+ceasarified+'"')
	
print('\nW2.D2.07 Ceaser Cypher (Optional)')
ceasarify()
input('\n>Press Enter to go to next exercise')

# W2.D2.08 Print list of list
	# #Write a function that prints out all elements of the above board, starting from the first element of the first line, 
	# till the end. Each line should be read from beginning to end.

def print_list_of_list():
	M = 'Land'
	o = 'Water'

	world = [[o,o,o,o,o,o,o,o,o,o,o],
	 [o,o,o,o,M,M,o,o,o,o,o],
	 [o,o,o,o,o,o,o,o,M,M,o],
	 [o,o,o,M,o,o,o,o,o,M,o],
	 [o,o,o,M,o,M,M,o,o,o,o],
	 [o,o,o,o,M,M,M,M,o,o,o],
	 [o,o,o,M,M,M,M,M,M,M,o],
	 [o,o,o,M,M,o,M,M,M,o,o],
	 [o,o,o,o,o,o,M,M,o,o,o],
	 [o,M,o,o,o,M,o,o,o,o,o],
	 [o,o,o,o,o,o,o,o,o,o,o]]


	for row in range (len(world)):
		for col in range (len(world[row])):
			print (world[row][col])
		print('\n')

print('\nW2.D2.08 Print list of list: print all elements in variable WORLD')
input('\n>Press Enter to display the result.')
print_list_of_list()
input('\n>Press Enter to go to next exercise')


#W2.D2.09 Print list of list on reverse.
	#Now write a function that prints out all elements in reverse.

def print_reverse():
	M = 'Land'
	o = 'Water'

	world = [[4,o,o,o,o,o,o,o,o,o,3],
	 [o,o,o,o,M,M,o,o,o,o,o],
	 [o,o,o,o,o,o,o,o,M,M,o],
	 [o,o,o,M,o,o,o,o,o,M,o],
	 [o,o,o,M,o,M,M,o,o,o,o],
	 [o,o,o,o,M,M,M,M,o,o,o],
	 [o,o,o,M,M,M,M,M,M,M,o],
	 [o,o,o,M,M,o,M,M,M,o,o],
	 [o,o,o,o,o,o,M,M,o,o,o],
	 [o,M,o,o,o,M,o,o,o,o,o],
	 [2,o,o,o,o,o,o,o,o,o,1]]

	r = len(world)-1
	c = len(world[0])-1

	for row in range (len(world)):
		for col in range (len(world[row])):
			print (world[r][c])
			c += -1
		
		r += -1
		c = len(world[0])-1
		

		print('\n')

print('\nW2.D2.09 Print list of list on reverse.')
input('\n>Press Enter to display the result.')
print_reverse()
input('\n>Press Enter to go to next exercise')


#W2.D2.10	Fix the Bug of Continent Counter
	#There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)
M = 'Land'
o = 'Water'

world = [[o,o,o,o,o,o,o,o,o,o,o],
		[o,o,o,o,M,M,o,o,o,o,o],
		[o,o,o,o,o,o,o,o,M,M,o],
		[o,o,o,M,o,o,o,o,o,M,o],
		[o,o,o,M,o,M,M,o,o,o,o],
		[o,o,o,o,M,M,M,M,o,o,M],
		[o,o,o,M,M,M,M,M,M,M,M],
		[o,o,o,M,M,o,M,M,M,o,o],
		[o,o,o,o,o,o,M,M,o,o,o],
		[o,M,o,o,o,M,o,o,o,o,o],
		[o,o,o,o,o,o,o,o,o,o,o]]

def continent_counter(world, x, y):


	if world[x][y] is not 'Land':
		return 0

	size = 1
	world[x][y] =  'counted'

	if x != 0 and y != 0:
		size = size + continent_counter(world, x-1, y-1)

	if y != 0:
		size = size + continent_counter(world, x , y-1)

	if y != 0 and x != len(world)-1:
		size = size + continent_counter(world, x+1, y-1)

	if x != 0:
		size = size + continent_counter(world, x-1, y)

	if x != len(world)-1:
		size = size + continent_counter(world, x+1, y)

	if x != 0 and y != len(world[x])-1:
		size = size + continent_counter(world, x-1, y+1)

	if y != len(world[x])-1:
		size = size + continent_counter(world, x, y+1)

	if x != len(world)-1 and y != len(world[x])-1:
		size = size + continent_counter(world, x+1, y+1)

	return size

print ('\nW2.D2.10 Fix the Bug of Continent Counter')
print('\nResult for x,y = 5,5 should be 25.\nResult is: ' + str(continent_counter(world,5,5)))
input('\n>Press Enter to go to next exercise')

#W2.D2.11	Random World Generated of "n" size
	# #Write a function that generates an n x n sized board with either land or water chosen randomly.
from random import choice

def random_world():

	M = 'Land'
	o = 'Water'

	n=0
	while n==0:
		n=int(input('\nEnter a number to print your world: '))
		
	list1=[]
	world=[]
	
	for row in range (0,n):
	 	for col in range (0,n):
	 		list1.append(choice([M,o]))
	 	world.append(list1)
	 	list1=[]

	print('\nRandom World Generated {}x{}.\n'.format(n,n))
	
	for z in world:
		print(" ".join(map(str, z)))

print('W2.D2.11	Random World Generated of "n" size plus Optional Advanced included - version 1')
random_world()
input('\n>Press Enter to go to next exercise')

#W2.D2.11	Random World Generated of "n" size
	# #Write a function that generates an n x n sized board with either land or water chosen randomly.
# Optional, Advanced
	# Run your continent counter for a 20 x 20 board. How long does it take to run? 
	#(If it runs quickly, try 30 x 30 ... 100 x 100 just be aware you might end up in a VERY LOOOONG WAIT) 
	#- make sure you know how to break a running program as it may take a long time to complete 
	#and you might not have time to wait for it ;)

from random import choice

def random_world():

	M = 'M' #Land
	o = 'o' #Water

	n=0
	while n==0:
		n=int(input('\nEnter a number to print your world: '))
		
	list1=[]
	world=[]
	
	for row in range (0,n):
	 	for col in range (0,n):
	 		list1.append(choice([M,o]))
	 	world.append(list1)
	 	list1=[]

	print('\nRandom World Generated {}x{}.\n'.format(n,n))
	print('Where "M" is Land and "o" is Water')

	for z in world:
		print(" ".join(map(str,z)))

print('\nW2.D2.11	Random World Generated of "n" size plus Optional Advanced included - version 2.')

random_world()
input('\n>Press Enter to go to next exercise')

# #WK2_D3
print('\nDay 3.\n')

#W2.D2.13	Modify Key in dict
	# Modify "a" for another name in my_dict. Hint: you will have to create a new key-value pair, copy in the value, and then delete the old one.

def modify_key():

	my_dict = {
	    "a": 35000,
	    "b": 8000,
	    "z": 450
	}

	print('Original Dictionary: \n'+str(my_dict))

	my_dict["new"]=my_dict["a"]# create a new copy and copy a: value
	del(my_dict["a"]) # delete key "a"

	print('\n"a" changed to "new":\n'+str(my_dict))

	return my_dict

print('W2.D3.13	Modify Key in dict')
input('\n>Press Enter to display the result.')
modify_key()
input('\n>Press Enter to go to next exercise')

#W2.D2.14 Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.
def freq_distribution2():
	
	filename = "alice_in_wonderland.txt"
	file = open(filename, encoding="utf8")

	counter={}
	#         01234567890123567890123456
	alphabet='abcdefghijklmnopqrstuvwxyz'
	
	#create dictionaty with alphabet
	for l in alphabet:
		counter[l]=0

	# print(counter)
	
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
	for c in counter:
		print(c+': '+str(counter[c]))


	return counter

print('\nW2.D3.14 Redo the frequency distribution of alice_in_wonderland.txt and save your result in a dictionary.')
input('\n>Press Enter to display the result.')
freq_distribution2()
input('\n>Press Enter to go to next exercise')


# W2.D3.15	Create a dictionary with your own personal details
	# feel free to be creative and funny so for example, 
	# you could include key-value pairs with quirky fact, fav quote, pet. Practice adding, modifying, accesing.
def personal_dict():
	#create:
	my_dict = {
				"First Name" : 'Jessica',
				"Last Name" : 'Sanchez'
	}
	
	print('\nCreate dictionary:')
	input('\n>Press Enter to display the result.')
	for m in my_dict:
		print(m + ': ' + str(my_dict[m]))

	#add:
	my_dict["Favorite quote"] = '"while (!succeed): try"'
	my_dict["Favorite Programming Languages"] = ['java','python','scala']
	my_dict["Favorite Morning habit"] = ['Morning Yoga', 'Meditation']

	print('\nAdd Values:')
	input('\n>Press Enter to display the result.')
	for m in my_dict:
		print(m + ': ' + str(my_dict[m]))

	#modify value:
	my_dict["First Name"] += " Abigail"
	my_dict["Last Name"] += " Cervantes"

	print('\nModify Values:')
	input('\n>Press Enter to display the result.')
	for m in my_dict:
		print(m + ': ' + str(my_dict[m]))

	#modify key:
	my_dict["Favorite Activities"] = my_dict["Favorite Morning habit"]
	del(my_dict["Favorite Morning habit"])

	print('\nModify Key:')
	input('\n>Press Enter to display the result.')
	for m in my_dict:
		print(m + ': ' + str(my_dict[m]))

	#delete key
	del(my_dict["Last Name"])

	print('\nDelete Key:')
	input('\n>Press Enter to display the result.')
	for m in my_dict:
		print(m + ': ' + str(my_dict[m]))

print('W2.D3.15	Create a dictionary with your own personal details')
personal_dict()
input('\n>Press Enter to go to next exercise')


# # Optional / Advanced
# W2.D3.16	Python the Hard Way ex. 39
	# Do Python the Hard Way ex. 39 exercises
	# # Mapping with cities and states/regions in your country or some other country.
	# # Find the Python documentation for dictionaries and try to do even more things to them.
	# # Find out what you can't do with dictionaries. A big one is that they do not have order, so try playing with that.

import pprint
def map_States():
	state_cc={'Aguascalientes' : 'Aguascalientes',
			'Baja California' : 'Mexicali',
			'Baja California Sur' : 'La Paz',
			'Campeche' : 'Campeche',
			'Coahuila' : 'Saltillo',
			'Colima' : 'Colima',
			'Chiapas' : 'Tuxtla Gutiérrez',
			'Chihuahua' : 'Chihuahua',
			'Distrito Federal' : 'Ciudad de México',
			'Durango' : 'Durango',
			'Guanajuato' : 'Guanajuato',
			'Guerrero' : 'Chilpancingo',
			'Hidalgo' : 'Pachuca',
			'Jalisco' : 'Guadalajara',
			'México' : 'Toluca',
			'Michoacán' : 'Morelia',
			'Morelos' : 'Cuernavaca',
			'Nayarit' : 'Tepic',
			'Nuevo León' : 'Monterrey',
			'Oaxaca' : 'Oaxaca',
			'Puebla' : 'Puebla',
			'Querétaro' : 'Querétaro',
			'Quintana Roo' : 'Chetumal',
			'San Luis Potosí' : 'San Luis Potosí',
			'Sinaloa' : 'Culiacán',
			'Sonora' : 'Hermosillo',
			'Tabasco' : 'Villahermosa',
			'Tamaulipas' : 'Ciudad Victoria',
			'Tlaxcala' : 'Tlaxcala',
			'Veracruz' : 'Xalapa',
			'Yucatán' : 'Mérida',
			'Zacatecas' : 'Zacatecas',
			}

	#for loop to print:
	print('\nUse for loop to  print')
	for s in state_cc:
		print('The Capital city of ' + s + ' is ' + state_cc[s])

	input('\n>Press Enter.')
	#use .get

	print('\n' + '-' * 10)
	print('Use .get ')
	print('Which is the capital city of Texas?')
	state = state_cc.get('Texas')

	if not state:
		print('Sorry, that is not a state in Mexico')

	#check length 
	print('check length')
	print('\n' + '-' * 10)
	print ('There are '+str(len(state_cc)) + ' states in Mexico.')

	#check if key exist in dict
	print('\n' + '-' * 10)
	if 'Zacatecas' in state_cc:
		print ('Zacatecas is a state of Mexico')


	#Get a value of a specified key
	print('\n' + '-' * 10)
	print (state_cc.get('Sonora'))

	#Print all key and values
	print('\n' + '-' * 10)
	print('Print all key and values')
	input('\n>Press Enter to display the result.')
	for key,val in state_cc.items():
		print(key,"=>",val)	

	#Get only the keys from the dictionary
	print('\nGet only the keys from the dictionary:\n')
	input('\n>Press Enter.')
	states = state_cc.keys()
	print('\nOption 1: ')
	print(states)

	print('\nOption 2: ')
	print('Mexico has these states: '," ".join(state_cc))
	
	print('\nOption 3: ')
	print('This dictionary contains these keys: '," ",state_cc.keys())

	#Printing the values
	print('\nPrinting the values')
	input('\n>Press Enter to display the result.')
	print("\nCapital Cities: \n"),
	for capitals in state_cc:
		c= state_cc[capitals]
		print(c)

	#with pprint (import pprint)
	print('\nWith pprint:')
	input('\n>Press Enter to display the result.') 
	pprint.pprint(state_cc)

	# Sorting the dictionary
	print('\n' + '-' * 10)
	print('Sorting the dictionary.')

	print('\nOption 1:')
	input('\n>Press Enter to display the result.')
	for key,value in sorted(state_cc.items()):
		print(key,value)

	print('\n Option 2:')
	input('\n>Press Enter to display the result.')
	for state in sorted(state_cc, key=len):
		print (state, state_cc[state])

	#Count
	print('\n' + '-' * 10)
	print('\nCounting:')
	count = {}
	for element in state_cc:
		count[element] = count.get(element,0) + 1
	print(count)

print('\nW2.D3.16	Python the Hard Way ex. 39\n')
input('\n>Press Enter to display the result.')
map_States()
input('\n>Press Enter to go to next exercise')

# W2.D3.19	Student Variable 
	# Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone 
	# who shared their dream.

from student import *

def create_Student():
	#name, discord_id, fav_food, dream
	s1 = Student("Andreea Visanoiu​", "Andreea[Gold]", "wontonmee", "teaching_university")
	s2 = Student("Cristina Tarantino", "CristyTarantino[Gold]", "Pasta" , "being an amazing developer")
	s3 = Student("Jessica Sanchez", "Jessi_RS [Gold]", "", "became a backend developer")
	s4 = Student("alteredco","alteredco [GOLD]","sushi","")
	s5 = Student("Marwa Qabeel​", "Marwa Qabeel [Gold]", "", "Data Analyst")
	s6 = Student("Sacha Young", "sacha[Gold]", "french fries", "to return to research")
	s7 = Student("Bituin Callanta", "bituin [gold]", "sashimi", "lessen the gender wage gap")
	
	students = [ s1, s2, s3, s4, s5, s6, s7]

	for s in students:
		Student.my_print(s) 
	
print('\nW2.D3.19 Student Variable\n')
create_Student()
input('\n>Press Enter to go to next exercise')


#W2.D3.20	1MWTT student into a Student class
	# # Translate the real world 1MWTT student into a Student class, decide on all the attributes that would be meaningful.
	# 	# Hint: You can start with the DIY signup form https://memberportal.1millionwomentotech.com/diy but feel free to be 
	# 	# creative and add/modify as you see it best! This is the REAL work of a creator to find the meaningful description 
	# 	# of reality and translate it for computers.
from diy import *

def new_diy():     
	first_n, last_n, email, country_code, tel, github, discord_id, country_birth, country_loc, gender, motivation, coding_level, groups, extra = "", "", "", "", "", "", "", "", "", "", "", "", "", ""

	print("\nPlease enter the following information to create your DIY account:\n")
	while first_n == "":
		first_n = input ('First Name: ')
	while last_n == "":
		last_n = input ('Last Name: ')
	while '@' not in email:
		email = input ('Email: ')
	print('Telephone number:')
	while country_code == "":
		country_code = input('\tCountry Code: (i.e. 001): ')
	while tel == "":
		tel = input('\tTelephone Number: ')

	github = input ('Github user ID, if not available press Enter: ')
	discord_id = input ('Discord_id, if not available press Enter: ')

	while country_birth == "":
		country_birth= input ('Country where you were born: ')

	country_loc == input ('If you live in a different country, please enter it, otherwise press Enter to continue: ')
	if country_loc == "":
		country_loc = country_birth

	print('How do you identify as?')
	while gender == "":
		answer = input ('\tType \'F\' for Femenine\n\tType \'M\' for Masculine\n\tnType \'N\' for None Binary\n\t> ')

		if answer.upper() == 'F':
			gender = 'Femenine'
		elif answer.upper() == 'M':
			gender = 'Masculine'
		elif answer.upper() =='N':
			gender = 'None Binary'

	while motivation == "":
		motivation = input ('\nWhy would you like to take this Online_Course: ')

	print('\nMy coding level is: ')
	print('B-Beginner    I- Intermediate    A-Advanced\n(Type only the first letter)')

	while coding_level == "":
		answer = input('> ')
		answer = answer.upper()
		if answer == "B":
			coding_level = 'Beginner'
		if answer == "I":
			coding_level = 'Intermediate'
		if answer == "A":
			coding_level = 'Advanced'

	print('\nI want to subscribe to and join the following groups:')
	print('Student, Working, Job seeking, Entrepreneur, Mom, Single Mom, Non-Binary, Trans, Retired, Career changer')
	print('Type a group name at a time and press Enter, or leave it blank to continue.: ')
	answer = " "
	while answer != "":
		answer = input('> ')
		if answer != "":
			groups += ' '+answer
		
	print('\nI would also like to support as:')
	print('Volunteer    Mentor    Hiring Company')
	print('Type a group name at a time and press Enter, or leave it blank to continue.: ')
	answer = " "
	while answer != "":
		answer = input('> ')
		if answer != "":
			extra += answer

	new_student= Diy(first_n, last_n, email, country_code, tel, github, discord_id, country_birth, country_loc, gender, motivation, coding_level, groups, extra)

	return new_student


print('\nW2.D3.20	1MWTT student into a Student class (DIY) ')

s1 = new_diy()

print('\nStudent 1')
Diy.my_print(s1)

s2 = Diy('Jess', 'Sanchez', 'jessica.sanchezc@gmail.com', '042',  '1917177980', 'jess', 'jess_rs', 'Mexico', 'Slovakia', 'Femenine', 'To get a job after completing it', 'Intermediate', 'Student', 'Volunteer')
print('\nStudent 2:')
Diy.my_print(s2)

print('\nCoded by Jessica Abigail Sanchez Cervantes for Summer of Code 2018 #1MWTT')

