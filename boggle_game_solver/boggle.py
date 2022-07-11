"""
File: boggle.py
Name: 雲筱涵
----------------------------------------
TODO: Find all words on the panel.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: Users give 4*4 board, find all words on board, and each word constructed from letters of i's neighbors.
	"""
	start = time.time()
	####################
	word_dict = {}  # All words dictionary from File
	read_dictionary(word_dict)
	input_lst = []  # User input list
	ans_lst = []    # Answer list
	# Create 4 *4 board
	for i in range(4):
		input_word = input(f'{i + 1} row of letters: ').lower()
		input_word = input_word.split()
		if len(input_word) == 4:
			for letter in input_word:
				if len(letter) != 1 or not letter.isalpha():
					print('Illegal input')
					return
			input_lst.append(input_word)
		else:
			print('Illegal input')
			return

	find_words(input_lst, word_dict, ans_lst)

	print(f'There are {len(ans_lst)} words in total. ')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(input_lst, word_dict, ans_lst):
	for i in range(len(input_lst)):
		for j in range(len(input_lst[i])):
			# 給每個字母x, y座標
			x = i
			y = j
			find_words_helper(x, y, input_lst, word_dict, ans_lst, '', [])


def find_words_helper(x, y, input_lst, word_dict, ans_lst, cur_s, used_index):
	# Base case
	if len(cur_s) >= 4:
		if cur_s in word_dict and cur_s not in ans_lst:
			ans_lst.append(cur_s)
			print('Found: ' + cur_s)

	for i in range(-1, 2):
		for j in range(-1, 2):
			neighbor_x = x + i
			neighbor_y = y + j
			if i == 0 and j == 0:
				if (x, y) not in used_index:
					used_index.append((x, y))
			# Out of range of panel
			if neighbor_x < 0 or neighbor_y < 0 or neighbor_x > len(input_lst)-1 or neighbor_y > len(input_lst)-1:
				pass
			else:
				if (neighbor_x, neighbor_y) not in used_index:
					# choose
					cur_s += input_lst[neighbor_x][neighbor_y]
					used_index.append((neighbor_x, neighbor_y))
					# explore
					if has_prefix(cur_s, word_dict):
						find_words_helper(neighbor_x, neighbor_y, input_lst, word_dict, ans_lst, cur_s, used_index)
					# un-choose
					cur_s = cur_s[:-1]
					used_index.pop()


def read_dictionary(word_dict):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			word_dict[word] = word


def has_prefix(sub_s, word_dict):
	"""
	:param word_dict: (dict) All word dictionary
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dict:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
