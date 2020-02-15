#! /usr/bin/env python
def get_divisors(n):
	divisors=[]
	for i in range(1,n):
		if n%i==0:
			divisors.append(i)
	divisors.append(n)
	return divisors

if __name__ == '__main__':
	n = abs(int(input("Give me a non-decimal number: ")))
	divisors = get_divisors(n)
	print('The divisors of ' + str(n) + ' are: ')
	print(divisors)
