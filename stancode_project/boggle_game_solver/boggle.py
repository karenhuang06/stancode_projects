"""
File: boggle.py
Name: Karnen Huang
----------------------------------------
This file helps user find word whose length is more than 4 and in dictionary by using 16 characters entered
by user.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
dic = []	 # contains all the word found in the dictionary txt file


def main():
	"""
	This function helps user find word whose length is more than 4 and in dictionary by using 16 letters entered
	by user.
	"""
	read_dictionary()
	while True:
		ch_lst = []
		for i in range(4):
			row = input(str(i+1) + ' row of letters: ').lower()
			if not correct_format(row):
				print('Illegal input')
				return
			ch = row.split()
			ch_lst.append(ch)

		word_lst = [] 				# contains all the word found in dic based on the letters entered by user
		num_lst = [0]				# records the number of word has printed

		# Make every letter entered by user become starting point
		for x in range(len(ch_lst)):
			for y in range(len(ch_lst)):
				find_boggle('', ch_lst, x, y, [(x, y)], word_lst, num_lst)  # start recursion
		print('There are', num_lst[0], 'words in total.')
		break


def correct_format(row):
	"""
	:param row: str, the data entered by user
	:return: bool, if the format of the data is correct
	"""
	if row[1] is not ' ' or row[3] is not ' ' or row[5] is not ' ':
		return False
	else:
		return True


def find_boggle(current_s, ch_lst, x, y, use_lst, word_lst, num_lst):
	"""
	:param current_s: str, contains the letters we choose and create a word
	:param ch_lst: lst, contains all the letters entered by user
	:param x: int, the position of the letter
	:param y: int, the position of the letter
	:param use_lst: lst, contains the position of letters contain in current_s
	:param word_lst: lst, contains all the word found in dic based on the letters entered by user
	:param num_lst: lst, records the number of word has printed
	:return: show all the word found in dic based on the letters entered by user in console
	"""
	# when length of current_s is more than 4,  consider to print current_s
	if len(current_s) >= 4:
		if current_s in dic:
			if current_s not in word_lst:
				print('Found "'+current_s+'"')
				word_lst.append(current_s)
				num_lst[0] += 1
				
	# find the letter next to the current position
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= x + i < 4:
				if 0 <= y + j < 4:
					# Choose
					if (x+i, y+j) not in use_lst:
						current_s += ch_lst[x+i][y+j]
						use_lst.append((x+i, y+j))
						# Explore
						if has_prefix(current_s):
							find_boggle(current_s, ch_lst, x+i, y+j, use_lst, word_lst, num_lst)
						# Un-choose
						current_s = current_s[:-1]
						use_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			dic.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
