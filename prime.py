#! /usr/bin/env python
'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below
'''

def is_prime(num):
	from divisors import get_divisors
	divisors = get_divisors(num)
	if divisors == [1,num]:
		prime = True
	else:
		prime = False
	return prime

if __name__ == '__main__':
	num = abs(int(input("Choose a number: ")))
	if is_prime(num) == True:
		print (str(num) + " is a prime number.")
	else:
		print (str(num) + " is not a prime number.")
