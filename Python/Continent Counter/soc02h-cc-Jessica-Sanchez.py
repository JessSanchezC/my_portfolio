##C:\Users\Public\Online_Courses\SOC\WK2
##6draftWK2_H.py

from random import randint
import mmap

def intro():
	print('\n**** WELCOME TO BOGGLE ****\n')
	print('After the board is shaken, you will have 3 minutes to write down all words you can see on the board.')
	print('\nPoints are given in the following way:')
	print('\t* 1 and 2 letter words = 0 points \n\t* 3 letter words = 1 point \n\t* 4 letter words = 2 points \n\t* 5 letter words = 3 points')
	print('\t* and so on...')
	print('\nThe longest possible word 16 letter word = 14 points')
	print('\nWhen you build a word, you can only use one letter once: in other words if you travel along the board \nand you used a letter, you cannot use it again for the same word, however, you CAN use it for a new word.')
	print('You can travel in any direction on the board, diagonal travel is allowed.')		

def get_size():
	n=int(input('\nSelect the size of the board from 3 to 5: '))
	if n<3 or n>5:
		get_size()
	else:
		return n

def dice(n):
	#dices (1-9) repeated to fill in the missing dices for 5x5 version (17-25)
	dices=[
		'AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW',
		'CIMOTU','DISTTY','EIOSST','DELRVY','ACHOPS',
		'HIMNQU','EEINSU','EEGHNW','AFFKPS','HLNNRZ',
		'DEILRX',
		'AAEEGN','ELRTTY','AOOTTW','ABBJOO','EHRTVW',
		'CIMOTU','DISTTY','EIOSST','DELRVY'
		]

	return dices[n]

def create_board(n):
	#board nxn
	dice_n=0
	board=[]
	row=[]
	
	for i in range (n):#build rows
		#build columns
		for j in range (n):
			r=randint(0,5)
			d=dice(dice_n)
			row.append(d[r])
			dice_n+=1
		board.append(row)
		row=[]
	return board

def board_copy(n,original):
	b=[]
	row=[]
	for i in range (n):#build rows
		#build columns
		for j in range (n):

			row.append(original[i][j])
		b.append(row)
		row=[]
	return b

def printBoard(board):
	print('\n')
	for x in board:
		print(" ".join(map(str, x)))
	print('\n')

def choose_dict():
	d=0
	print('\nWhich dictionary would you like to use:')
	print('\nOption1: Scrabble_Bot.     Option2: Words_Alpha.')
	while d<1 or d>2:		
		d=int(input('\n      Enter 1 or 2: '))
	result =d

def get_dictionary(d):
	#https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
	option1 = "dictionary.txt"
	option2 = "dictionary.txt"#Word Alpha is in low caps and different format :(
	if d == 1 :
		filename=option1
	else :
		filename=option2
	file = open(filename,"r")
	# raw = file.read()
	#print(raw)
	return file

def get_user_list():
	user_words={}
	print('\nThis is your board: ')
	printBoard(board)
	print('You have 3 minutes to enter your words, enter one word at a time and press enter to add a new word. \nWhen finished press Enter.')
	n=' '
	words=[]
	while n!='':
		n=input('>')
		if n!='':
			if n.upper() not in words:
				user_words[n.upper()]=''#add to user words dict with blank score
				words.append(n.upper()) #add to list of words
	user_words['WORDS']=sorted(words)
	return user_words

def print_dict(d):
	print('\n')	
	for w in d:
		print(w+': '+str(d[w]))

def validate_list(words):
	score=0
	w_in_dict=word_in_dictionary(words)## {word:boolean}
	for w in words:
		print('Validating word: '+w+'...')
		if w_in_dict[w]  and word_in_board(w):
			if len(w)<=2:
				user_list[w]=0
			else:
				user_list[w]=len(w)-2
				score+=len(w)-2
		elif w_in_dict[w]==False:
			user_list[w]='not in dictionary'	
		elif word_in_board(w)==False:
			user_list[w]='not in board'
		else:
			user_list[w]=0
		user_list['Total Score']=score

def word_in_dictionary(words):
	# in_dict=False
	w2={} #word:TRUE, word:FALSE
	for w in words:
		w2[w]=False

	for line in file:
		l=file.readline()
		for w in words:
			if l==w:
				w2[w]=True
				#print(w+' in dictionary: '+l)
			else:
				l=l[:len(l)-1]
				if l==w:
					w2[w]=True
					#print(w+' in dictionary: '+l)

	return w2

def word_in_board(word):
	is_in_board=False
	for row in range (len(board)):
		for col in range (len(board)):
			if word[0] == board[row][col]:
				#print('word '+word+' starts in row:'+str(row)+' col:'+str(col)+" with char: " + board[row][col])
				#print('check_around')
				board2=board_copy(n,board)
				if check_around(word[1:],row,col,board2)==True:
					is_in_board=True
					return is_in_board

	#print('word '+word+' in board: '+str(is_in_board) )
	return is_in_board

def check_around(word,row,col,board2):
	#LEFTUP=>UP=>RIGHTUP=>RIGHT=>DOWNRIGHT=>DOWN=>DOWNLEFT=>LEFT
	#printBoard(board2)
	char_in_board = False
	r = row
	c = col

	if board2[row][col] == ' ':
		board2=board
		return char_in_board
	
	board2[row][col]=' '
	##BUG SOLVED!! if 2 or more letters around the box are the same!! i.e: FOOLS
	# E E W J H
	# U T I D A
	# I E G F L
	# X E E O O
	# R I Y S L

	#upper levels
	if row != 0 and col != 0 and board2[row-1][col-1] == word[0]:#leftup
		char_in_board=True #if char in dice, TRUE
		r=row-1
		c=col-1
		#print('leftup checked for '+ word[0]+' and it\'s true')
		
	if row != 0 and board2[row-1][col] == word[0]: #up
		if 	char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:], row-1, col,b): #another letter around was matching
				#print('Check finished')
				return char_in_board	
		else:		
			char_in_board=True
			r=row-1
			c=col
			#print('up checked for '+ word[0]+' and it\'s true')
		
	if row != 0 and col != len(board2)-1 and board2[row-1][col+1] == word[0]: #rightup
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row-1,col+1,b):
				#print('Check finished')
				return char_in_board
		else:	
			char_in_board=True
			r = row-1
			c = col+1
			#print('rightup checked for '+ word[0]+' and it\'s true')
		
	if col != len(board2)-1 and board2[row][col+1] == word[0]:#right
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row,col+1,b):
				#print('Check finished')
				return char_in_board	
		else:
			char_in_board=True
			r = row
			c = col+1
			#print('right checked for '+ word[0]+' and it\'s true')
			
	#lower levels
	if row != len(board2)-1 and col != len(board2)-1 and board2[row+1][col+1] == word[0]:#rightdown
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row+1,col+1,board2):
				#print('Check finished')
				return char_in_board	
		else:
			char_in_board=True
			r = row+1
			c = col+1
			#print('rightdown checked for '+ word[0]+' and it\'s true')
		
	if row != len(board2)-1 and board2[row+1][col] == word[0]:#down
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row+1,col,board2):
				#print('Check finished')
				return char_in_board	
		else:
			char_in_board=True
			r = row+1
			c = col
			#print('down checked for '+ word[0]+' and it\'s true')
		
	if row != len(board2)-1 and col != 0 and board2[row+1][col-1] == word[0]: #leftdown
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row+1,col-1,board2):
				#print('Check finished')
				return char_in_board	
		else:
			char_in_board=True
			r = row+1
			c = col-1
			#print('leftdown checked for '+ word[0]+' and it\'s true')
			
	if col != 0 and board2[row][col-1] == word[0]: #left
		if char_in_board == True and len(word) > 1:
			b=board_copy(n,board2)
			if check_around(word[1:],row,col-1,board2):
				# print('Check finished')
				return char_in_board	
		else:
			char_in_board=True
			r = row
			c = col-1
			# print('left checked for '+ word[0]+'and it\'s true')
				
	
	#print(board2)
	
	if len(word)==1 or char_in_board == False:
	#if last char in word or no char in boxes aroun, END
		# print('Check finished')
		return char_in_board
	else:
		# print('char '+word[0] +' in dice '+str(r)+','+str(c)+'. CHECK AROUND')
		char_in_board=check_around(word[1:],r,c,board2) #Recurrance

	return char_in_board


#Step 1: Intro get input from user (board size)
intro()
n=get_size()

#Step 2: Choose Dictionary
d=choose_dict()
file=get_dictionary(d) ##user better capslock
#ready?

#Build Board
board = create_board(n)
#board_letters=singleLetters()

#get wordlist from user
print(input('\nAre you ready? Press Enter to Shake the Board....'))
user_list=get_user_list()
words=user_list['WORDS']
words.sort()
#print('words: '+str(words))
del(user_list['WORDS'])

print('\n\nCalculating your score...\n')

#validate list and get score
validate_list(words)
print_dict(user_list)


def result_boggle():
	result={}
	result["score"]=user_list['Total Score']
	result["words"]=words
	return result

result=result_boggle()
print(result)

#*** see max score possible:



