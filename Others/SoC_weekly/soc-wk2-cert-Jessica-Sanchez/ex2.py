#C:\Users\Public\Online_Courses\SOC\WK2\wk2_HW
#ex2.py

# W2.D2.12 Continent Counter Test
	# Write test coverage in unittest and/or trace for Continent Counter.

def create_w():
	world=	[
			['o','X','o','o','o','o','o','o','o','o','o'],
			['o','X','X','X','X','X','o','o','o','o','o'],
			['o','X','X','X','X','X','o','o','o','X','X'],
			['X','X','X','X','X','X','o','o','o','o','o'],
			['X','o','X','X','X','o','o','o','o','o','o'],
			['X','o','o','X','o','o','o','o','o','o','o'],
			['X','X','X','o','o','o','o','o','o','X','X'],
			['o','o','o','o','X','X','X','X','X','X','o'],
			['o','o','o','o','X','X','X','X','X','X','o'],
			['o','o','o','o','o','o','X','X','X','X','o'],
			['o','o','o','o','o','X','X','o','o','o','o']
			]
	return world

def create_w2():
	world2=[[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0]]
	return world2

world = create_w()

n=11 ##11x11, or request to user the parameter to create random world with sixe defined by user

#Print the world(s)
def printWorld(world):
	print('\n')
	for x in world:
		print(" ".join(map(str, x)))
	print('\n')


def check_world(world2,row,col):
	#step 1 change world 2: if land change to number 1	
	if world[row][col] == 'o' or world2[row][col] == 1: # stop if water
		return 0

	world2[row][col] = 1
	
	if row != 0:#upper levels:

		if col != 0 and world2[row-1][col-1] != 1:#left-up
			check_world(world2,row-1,col-1)

		if world2[row-1][col] != 1: #up
			check_world(world2,row-1,col)

		if col!=n-1 and world2[row-1][col+1] != 1: #right-up
			check_world(world2,row-1,col+1)
	
	#sides:
	
	
	if col != 0 and world2[row][col-1] != 1:  #left
		check_world(world2,row, col-1)

	if col!=n-1 and world2[row][col+1] != 1: #right
		check_world(world2,row, col+1)
	
	if row != n-1: #down level:

		if col != 0 and world2[row+1][col-1] != 1: #left-down
			check_world(world2,row+1, col-1)

		if world2[row+1][col] != 1: #down
			check_world(world2,row+1,col)
		
		if col!=n-1 and world2[row+1][col+1] != 1: #right
			check_world(world2,row+1, col+1)#right-down



def continent_counter(row,col):
	#count ith a for loop the size
	world2 = create_w2()
	check_world(world2,row,col)
	# printWorld(world)
	# printWorld(world2)
	size = 0

	for row in world2:
		for col in row:
			size+= col
		# 	print('*')
		# print('-'*15)
	
	# print(size)
	return size

# continent_counter(1,1) # ==26
# continent_counter(6,10) # ==20
# continent_counter(2, 9) # ==2



	
