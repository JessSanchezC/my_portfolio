# #python soc-wk1-cert-Jessica-Sanchez_v2.py

#Old-school Roman numerals. extract
	#In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
	#No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
	#Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper 
	#old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
	#Make sure to test your method on a bunch of different numbers.
	#Hint: Use the integer division and modulus methods.
	#For reference, these are the values of the letters used: 

	

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


#“Modern” Roman numerals. 
	#Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had 
	#to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return 
	#the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
	
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

def play():
	#Run Old Roman
	print('OLD ROMAN')
	original=getnum()
	roman=convert_to_roman(original)
	print('\nThe equivalent Old Roman Numeral for '+str(original)+' is: '+ roman)

	# print(input('\nPress enter to continue.'))

	print('NEW ROMAN')
	original=getnum()
	roman=convert_to_roman2(original)
	print('\nThe equivalent Modern Roman Numeral for '+str(original)+' is: '+ roman)

