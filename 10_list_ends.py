#! /usr/bin/env python
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def list_ends(a_list):
	ends = [a_list[0] , a_list[-1]]
	return ends

if __name__ == '__main__':
	a = [5, 10, 15, 20, 25]
	print (list_ends(a))
