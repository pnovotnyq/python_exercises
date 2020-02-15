#! /usr/bin/env python
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

import random

a=[]
b=[]

for num in range(10):
	a.append(random.randint(1,101))
for num in range(20):
	b.append(random.randint(1,101))
print('List a: \n' + str(a))
print('List b: \n' + str(b))



# Will go through list a and search for each number in list b. Removes found numbers from list b to properly handle duplicates.

ab=[]
for i in a:
	if i in b:
		ab.append(i)
		b.remove(i)
print('Intersection of a and b: \n' + str(ab))


# Will create sets, where all numbers are unique - if a number appeared twice in each list, it would only be displayed once. It's also a one-liner.

#print(set(a).intersection(set(b)))


