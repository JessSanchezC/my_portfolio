# #python soc-wk1-cert-Jessica-Sanchez_v2.py
from random import choice, randint
import datetime

##Day1
print('\nDAY 1')
print('Hours in a year: ',24*365)
print('Minutes in a decade: ', (60*24*365*10))

mininsec=60
hrinsec=mininsec*60
dayinsec=hrinsec*24
yrinsec=dayinsec*365

print('My age in seconds (36yo): ',(yrinsec*36))
print('Calculate @Andreea Visanoiu\'s age: 48618000 seconds old is equivalent to',(48618000/yrinsec))

# print('How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?')
# print('How about a 64-bit system?')

# print('Calculate your age accurately based on your birthday')
b_date=datetime.date(1982,3,17) ##1982-03-17
today = datetime.date.today() ## i.e. 2018-07-18
my_age=(today-b_date).total_seconds()
print('My age(36yo) in seconds is {}'.format(my_age))

print(input('\nPress enter to continue.'))
##Day2-nothing

##Day3
print('\nDAY 3')
#Full name greeting. #Finally, it should greet the person using their full name.

print('\nFull Name Greeting.\n')
first=input("Please enter your First Name: ")
middle=input("Please enter your Middle Name, if none just press enter: ")
last=input("Please enter your Last Name: ")
print('Nice to meet you {} {} {}.'.format(first,middle,last) )
print(input('\nPress enter to continue.'))

#Bigger, better favorite number. 
	#Write a program that asks for a person’s favorite number. 
	#Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. 
	#(Do be tactful about it, though.)
print('\nBigger, better favorite number.\n')

favorite=int(input("{}, which is your favorite number? ".format(first)))
print('Well, I prefer {}, it\'s bigger and better, maybe you can consider it as your new favorite number.'.format(favorite+1))
print(input('\nPress enter to continue.'))

##Angry boss. 
	#Write an angry boss program that rudely asks what you want. 
	#Whatever you answer, the angry boss should yell it back to you and then fire you. 
	#For example, if you type in I want a raise, it should yell back like this: WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
print('\nAngry boss.\n')
print('\nYour Boss:"Are you playing with the computer?! Why are you not working?"')
request=input('You:> ')
print('Your Boss: "What?! What do you mean "{}"!! Go Back To Work Right Now!!"'.format(request))
print(input('\nPress enter to continue.'))

##write a program that will display a table of contents
def table():
	print('\n\nTable of Contents\n')
	print('Chapter 1: Getting Started {:.>12}\nChapter 2: Numbers {:.>20}\nChapter 3: Letters {:.>21}'.format('page 1','page 9','page 13'))
table()
print(input('\nPress enter to continue.'))

# try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly
n=11
def generateLand():
	list1=[]
	for i in range (0,n):
	 	list1.append(choice(['X','o']))
	 	##list1.append(random.randint(0, 1))
	return list1
 
world=[]
for i in range (0,n):
 	world.append(generateLand())

print('\nRandom World Generator\n')
for z in world:
	print(" ".join(map(str, z)))
print(input('\nPress enter to continue.'))

##DAY4:
print('\nDAY 4:\n')

#“99 Bottles of Beer on the Wall.” 
	#Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
print(input('99 Bottles of Beer lyrics\n>'))
def bottles() :
	count=99
	text1=' bottles of Beer'
	text2=' on the wall'
	text3=text1+text2
	text4='Take one down and pass it around, '
	text5='no more'
	text6='Go to the store and buy some more, '
	#99 bottles of beer on the wall, 99 bottles of beer.
	#Take one down and pass it around, 98 bottles of beer on the wall.
	
	for x in range(1,99):
		print(str(count)+text3+', '+str(count)+text1+'.')
		count-=1
		print(text4+str(count)+text3+'.\n')

	#1 bottle of beer on the wall, 1 bottle of beer.
	#Take one down and pass it around, no more bottles of beer on the wall.
	print(str(count)+text3+', '+str(count)+text1+'.')
	print(text4+text5+text3+'.\n')

	#No more bottles of beer on the wall, no more bottles of beer. 
	#Go to the store and buy some more, 99 bottles of beer on the wall.
	print(text5.capitalize()+text3+', '+text5+text1+'.')
	print(text6+str(99)+text3+'.\n')	
	print()

bottles()

print(input('\nPress enter to continue.'))
#Deaf grandma. 
	#Whatever you say to Grandma (whatever you type in), 
	#she should respond with this: HUH?! SPEAK UP, GIRL!
	#unless you shout it (type in all capitals). 
	#If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938!
	#o make your program really believable, have Grandma shout a different year each time, 
	#maybe any year at random between 1930 and 1950. 
	#(This part is optional and would be much easier if you read the section on Python’s random number generator under the Math Object.) 
	#You can’t stop talking to Grandma until you shout BYE.
#Deaf grandma extended. 
	#What if Grandma doesn’t want you to leave? 
	#When you shout BYE, she could pretend not to hear you. 
	#Change your previous program so that you have to shout BYE three times in a row. 
	#Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.

print('\nDeaf Grandma + extended.')
print('Chat with Grandma, if she can not hear you try to SHOUT!')
def chat(bye=0):	
	phrase=input('> ')
	if phrase=='BYE':
		bye+=1
	else:
		bye=0
		
	if bye==3:
		print('BYE MY DEAR! LOVE YOU!')
	else:
		answer=str(grandma(phrase))
		print('Grandma> '+ answer)
		chat(bye)

def grandma(phrase):
	#if not shouting to Grandma
	what1= "WHO IS IN THERE?!"
	what2= "HUH?! SPEAK UP, GIRL!"
	what3= "WHY ARE YOU WHISPERING?!"
	what=what1,what2,what3
	#If shouting to Grandma
	reply1= "YES! LET'S PLAY BINGO!"
	reply2= "NO! TODAY IS THURSDAY!"
	reply3= "NO SUGAR, PLEASE!"
	reply4= "YES, WITH MILK PLEASE"
	reply5= "UFF! IT WASN'T ME! "
	reply6= "NO SINCE 1970's"
	reply=reply1,reply2,reply3,reply4,reply5

	if phrase.isupper():
		answer=reply[randint(0,len(reply)-1)]
	else:
		answer=what[randint(0,len(what)-1)]
	return answer

chat()

print(input('\nPress enter to continue.'))
#Leap years. 
	#Write a program that asks for a starting year and an ending year and then puts all the leap years between them 
	#(and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). 
	#However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 
	#(such as 1600 and 2000, which were in fact leap years). What a mess!
print('\nLeap Years: This program will return the leap years between a starting and ending year, including them.\n')

def getYear(type):
	if type=='start':
		year=int(input('Enter a starting year(yyyy): '))
	elif type=='end':
		year=int(input('Enter an ending year(yyyy): '))
	return year

start=getYear('start')
end=getYear('end')
while end<start:
	print('Incorrect period entered, ending year should be larger than the starting year, please try again.')
	end=getYear('end')

print('The selected period starts on {} and ends on {}.'.format(start,end))

leapyears=[]
for y in range(start,end+1): 
	if y%4==0:
		if y%400==0:
			leapyears.append(y)
		elif y%100!=0:
			leapyears.append(y)
print('The leap years within this period are:')
print(leapyears)
print(input('\nPress enter to continue.'))

#Find something today in your life, that is a calculation. 
	#Go for a walk, look around the park, try to count something. 
	#Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, 
	#estimate your books by bookshelf, toiletries, wardrobe.
print('\nSomething Countable: Apple Tree')
print('This is inpired by an Apple Tree near my place, the program counts how many apples (\'0\') are on the tree and how many have fallen to the ground\n')

garden=['@','@','@',0,'@','@','@','@','@','@','@'],['@','@','@','@','@','@','@','@',0,'@',0],['@',0,'@','@','@','@','@','@','@','@','@'],['@','@','@',0,'@','@',0,'@',0,'@','@'],['@','@','@','@',0,'@','@','@','@','@','@'],['@',0,'@','@','@','@','@','@',0,'@',0],['@','@','@','@','@',0,'@','@','@','@','@'],[' ',' ',' ',' ','|','|',' ',' ',' ',' ',' '],[' ',' ',' ',' ','|','|',' ',0,' ',' ',' '],[0,' ',0,' ','|','|',' ',' ',' ',' ',' '],[' ',0,' ',' ','|','|',' ',' ',0,0,' ']

def printgarden(garden):
	for g in garden:
		print(" ".join(map(str, g)))
printgarden(garden)	

#tree is from row 0 to 6, count fallen apples from row 7 till 10
tree=0
fallen=0
for row in range (0,11):
	for col in range (0,11):
		if garden[row][col]==0:
			if row<=6:
				tree+=1
			else:
				fallen+=1

print('\n1. Apples on the Tree: ' + str(tree))
print('2. Apples on the ground: ' + str(fallen))
print(input('\nPress enter to continue.'))
#Building and sorting an array. 
	#Write the program that asks us to type as many words as we want 
	#(one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us 
	#in alphabetical order. Make sure to test your program thoroughly; 
	#for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?

def sortwords():
	print('\nCreate a list of words, and I will return it in alphabetical order.\nEnter one word at a time (press enter).\n')
	word=''
	word_list=[]
	while len(word_list)<2:
		word=input('Enter a word: ')
		if len(word)>0:
			word_list.append(word.capitalize())
	while len(word)>0:
		word=input('next: ')
		if len(word)>0:
			word_list.append(word.capitalize())
	word_list=sorted(word_list)
	print('\nThis is your list:')
	for w in word_list:
		print(w)

sortwords()

print(input('\nPress enter to continue.'))
#Table of Contents2
	#Write a table of contents program here. 
	#Start the program with a list holding all of the information for your table of contents 
	#(chapter names, page numbers, and so on). 
	#Then print out the information from the list in a beautifully formatted table of contents. 
	#Use string formatting such as left align, right align, center.
toc2=[]	
def add_content(content):#[0]Chapter No., #Chapter Title, #page
	toc2.append(content)

add_content([1,'Getting Started',12])
add_content([2,'Numbers',20])
add_content([3,'Letters',21])

def printToC(tableofcontent):
	print('\nTable of Content 2\n')
	for row in range (len(toc2)):
		print('    Chapter '+ str(toc2[row][0])+ ': '+toc2[row][1]+'{:.>20}'.format(toc2[row][2])     )

printToC(toc2)

print(input('\nPress enter to continue.'))
#Moo
	#Write a function that prints out "moo" n times.
print('\nMoo')
def moo(n):
	for x in range (n):
		print('{}. moo'.format(x+1))
n = int(input('How many times does the cow says Moo? Enter a number: '))
moo(n)

print(input('\nPress enter to continue.'))
#Old-school Roman numerals. 
	#In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
	#No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
	#Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper 
	#old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
	#Make sure to test your method on a bunch of different numbers.
	#Hint: Use the integer division and modulus methods.
	#For reference, these are the values of the letters used: 

	
print('\nOld-school Roman numerals.\n\nThis program will return the old Roman numeral equivalent to the number you will enter.')

def getnum(): #check if num within parameter 1 to 3000
	num = int(input('\nPlease Enter a number between 1 and 3000: '))
	if num > 3000 or num < 1:
		getnum()
	else:
		return num

##I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000

def getletter(x):
	roman=''
	n=0 
	letter=''
	#start from higher values....
	if x>=1000:
		n=1000
		letter='M'
	elif x>=500:
		n=500
		letter='D'
	elif x>=100:
		n=100
		letter='C'
	elif x>=50:
		n=50
		letter='L'
	elif x>=10:
		n=10
		letter='X'
	elif x>=5:
		n=5
		letter='V'
	elif x<5:
		n=1
		letter='I'
	result=n,letter
	return result

def convert_to_roman(x,roman=''):
	if x==0:
		return roman

	n=getletter(x)[0]
	letter=getletter(x)[1]
	
	r=x%n #remainder
	y=int((x-r)/n) #define the number of letters in roman numeral
	
	roman+=(letter*y)
##	print('\nx = '+str(x)+'\nn = '+str(n)+'\nletter= '+letter+'\nr = '+str(r)+'\ny = '+str(y)+'\nroman = '+roman)
	roman = convert_to_roman(r,roman)
	return roman
	
original=getnum()
roman=convert_to_roman(original)
print('\nThe equivalent Old Roman Numeral for '+str(original)+' is: '+ roman)


print(input('\nPress enter to continue.'))
#“Modern” Roman numerals. 
	#Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had 
	#to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return 
	#the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
	
print('\n“Modern” Roman numerals.\n\nThis program will return the Modern Roman numeral equivalent to the number you will enter.')
##I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000

def getletter2(x):
	roman=''
	n=0 
	letter=''
	#start from higher values....
	if x>=1000:
		n=1000
		letter='M'
	elif x>=900:
		n=900
		letter='CM'
	elif x>=500:
		n=500
		letter='D'
	elif x>=400:
		n=400
		letter='CD'
	elif x>=100:
		n=100
		letter='C'
	elif x>=90:
		n = 90
		letter='XC'
	elif x>=50:
		n=50
		letter='L'
	elif x>=40:
		n=40
		letter='XL'
	elif x>=10:
		n=10
		letter='X'
	elif x>=9:
		n=9
		letter='IX'
	elif x>=5:
		n=5
		letter='V'
	elif x>=4:
		n=4
		letter='IV'
	elif x<4:
		n=1
		letter='I'
	result=n,letter
	return result

def convert_to_roman2(x,roman=''):
	if x==0:
		return roman

	n=getletter2(x)[0]
	letter=getletter2(x)[1]
	
	r=int(x%n) #remainder
	y=int((x-r)/n) #define the number of letters in roman numeral
	
	roman+=(letter*y)
	##	print('\nx = '+str(x)+'\nn = '+str(n)+'\nletter= '+letter+'\nr = '+str(r)+'\ny = '+str(y)+'\nroman = '+roman)
	
	roman=convert_to_roman2(r,roman)
	return roman

original=getnum()
roman=convert_to_roman2(original)
print('\nThe equivalent Modern Roman Numeral for '+str(original)+' is: '+ roman)

print('\n\n******Coded by Jessica Abigail Sanchez Cervantes for Summer of Code 2018*****')