#! /usr/bin/env python
intro = '''
This is the game of cows and bulls. You are to guess the correct sequence of n random digits, where n is the difficulty of your choice.
Each correctly placed digit counts as a cow.
Each digit that belongs to the set of digits, but is not in the correct place counts as a bull.
'''

import random
import os, sys, time

def set_difficulty():
	difficulty = abs(int(input(
'''
Set difficulty:
3 - Very Easy
4 - Easy
5 - Moderate
6 - Hard\n
''')))
	os.system('clear')
	return difficulty

def get_random_numbers(difficulty):
	random_number_list = []
	for i in range(difficulty):
		random_number_list.append(random.randint(0,9))
	return random_number_list

def get_user_numbers(r_nums,difficulty):
	raw_user = input('\nPlease enter ' + str(difficulty) + ' digits or type "quit" to give up\n')
	if raw_user[0].lower() == 'q' or raw_user[0].lower() == 'e':
		print('The correct sequence was ' + str(r_nums) + ' .')
		print('Bye!')
		sys.exit()
	else:
		u_nums_list = list(raw_user.replace(' ',''))
		u_nums = [int(i) for i in u_nums_list] 
		if len(u_nums) != difficulty: 
			raise ValueError
		return u_nums

def evaluate(r_nums , u_nums, difficulty):
	cows = 0
	raw_bulls = 0
	for i in range(difficulty):
		if u_nums[i] == r_nums[i]:
			cows += 1
	for i in u_nums:
		if i in r_nums:
			raw_bulls += 1
	bulls = raw_bulls - cows
	return {'cows' : cows , 'bulls' : bulls}

def replay():
	answer = str(input('Would you like to play again? '))[0].lower()
	if answer == 'y' or answer == '1': 
		return True
	else:
		return False	

def main():
	tries = 0
	try:
		difficulty = set_difficulty()
	except ValueError:
		print('Please enter numbers.\n')
		main()
	r_nums = get_random_numbers(difficulty)
	while True:
		try:
			u_nums = get_user_numbers(r_nums,difficulty)
			tries += 1
			result = evaluate(r_nums , u_nums, difficulty)
			if result['cows'] == difficulty:
				print('\nYou win! And it only took you ' + str(tries) + ' tries.')
				if replay() == True:
					main()
				else:
					print('Bye!')
					sys.exit()
			else:
				print('Cows: ' + str(result['cows']))
				print('Bulls: ' + str(result['bulls']))
		except ValueError:
			print('Sorry, you have to enter ' + str(difficulty) + ' digits. Try again.')

os.system('clear')
print(intro)
time.sleep(8)
main()
