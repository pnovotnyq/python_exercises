#! /usr/bin/env python
'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''


n=abs(int(input('Insert a non-decimal number: ')))
def get_divisors(n):
	divisors=[]
	for i in range(1,n):
		if n%i==0:
			divisors.append(i)
	divisors.append(n)
	return divisors
divisors = get_divisors(n)
print('The divisors of ' + str(n) + ' are: ')
print(divisors)
