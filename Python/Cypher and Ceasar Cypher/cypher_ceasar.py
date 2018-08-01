#W2.D2.06 Cypher
# #Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
def cypher():
	
	message = input('\nType a message and it will be turned into numbers: ')
	c_message=[]
	
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
