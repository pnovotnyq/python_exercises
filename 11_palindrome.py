#! /usr/bin/env python
'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

def is_palindrome(word):
	reverse = word[::-1]
	if word.lower() == reverse.lower():
		palindrome = True
	else:
		palindrome = False
	return palindrome

if __name__ == '__main__':
	a = input("Type in a word: ")
	if is_palindrome(a) == True:
		print(a + " is a palindrome.")
	else:
		print(a + " is not a palindrome.")
	
