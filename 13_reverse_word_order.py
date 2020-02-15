#! /usr/bin/env python
'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
'''
if __name__ == '__main__':
	words = input('Type in a few words and I will reverse the word order: ')
	print(reverse_words(words))
def reverse_words(words):
	# Splits the string into words, and feeds them in reverse order while joining with a ' '
	return ' '.join(words.split()[::-1])

