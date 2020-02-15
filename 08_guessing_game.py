#! /usr/bin/env python
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
tries = 0
correct = 0

while True:

	target_num = random.randint(1,9)
	num = input("Pick a non-decimal number from 1 to 9 or type 'exit' to end: ")
	if num.lower() == 'exit':
		print("You tried to guess the number " + str(tries) + " times.")
		print("You had " + str(correct) + " correct guess/es.")
		break
	elif 1 <= int(num) <= 9:
		tries = tries + 1
		if int(num) > target_num:
			print ("You picked a higher number. \nThe correct number was: " + str(target_num))
		elif int(num) < target_num:
			print ("You picked a lower number. \nThe correct number was: " + str(target_num))
		else:
			print ("You guessed the right number!")
			correct = correct +1
	else:
		print ('Please enter a number between 1 and 9.')
