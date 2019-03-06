"""A simple Binary and Hex Converter in Python"""

__author__ = "Anderson S. Freixo <anderson.freixo@gmail.com>"


def prettify_bin(raw_str):
	"""Transforms the raw string of '0' and '1' given by dec_to_bin() 
into a more readable form by separating the bits in groups of fours"""

	pretty_bin = ''	
	#First, add leading zeros to the original string 
	#if the leftmost group has less than four bits

	while len(raw_str) %4 > 0:
		raw_str = "{}{}".format('0',raw_str)

	#Then put the characters in the new variable
	#adding a space after each group of four bits	
	for bit in range(len(raw_str)):
		if (bit)%4 == 0:
			pretty_bin+=' '
		pretty_bin+=raw_str[bit]
	return pretty_bin

def dec_to_bin(decimal):
	"""Converts a number from base 10 to base 2"""
	binary = ''
	while decimal > 0:
		binary+= str(decimal%2)
		decimal//= 2

	return prettify_bin(binary[::-1]) 
			

def dec_to_hex(decimal):
	"""Converts a number from base 10 to base 16"""
	hexa = ''
	symbols = '0123456789ABCDEF'
	while decimal > 0:
		hexa+= symbols[decimal%16]
		decimal//=16
	return hexa[::-1]

if __name__ == '__main__':
	dec_to_hex(50)
	for num in range(0,1025):
		print("{}: {} - {}".format(num, dec_to_bin(num), dec_to_hex(num)))


