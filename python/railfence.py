
# Rail Fence Cipher


# function to encrypt a message
def encryptRailFence(text, key):

	rail = [['\n' for i in range(len(text))]
				for j in range(key)]
	
	# to find the direction
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		# fill the corresponding alphabet
		rail[row][col] = text[i]
		col += 1
		
		# find the next row using
		# direction flag
		if dir_down:
			row += 1
		else:
			row -= 1
	# now we can construct the cipher
	# using the rail matrix
	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))
	

def decryptRailFence(cipher, key):

	
	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	
	# to find the direction
	dir_down = None
	row, col = 0, 0
	
	# mark the places with '*'
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		
		# place the marker
		rail[row][col] = '*'
		col += 1
		
		
		if dir_down:
			row += 1
		else:
			row -= 1
			
	
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	
	# zig-zag 
	
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		
		# check the direction of flow
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
			
		# place the marker
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		# find the next row using
		# direction flag
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))


if __name__ == "__main__":
	
	print("Encode:",encryptRailFence("Augustismybirthdaymonth", 3))
	
	
	# Now decryption of the
	# same cipher-text
	print("Decode:" ,decryptRailFence("ausidoussimbrhamnhgtytyt", 3))
	

