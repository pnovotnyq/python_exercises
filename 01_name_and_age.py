#! /usr/bin/env python
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


datetime
input()
string manipulation
'''

import datetime

current_year=datetime.datetime.now().year
age = int(input('Enter your age: '))
if age >= 100:
	print("Please enter a number below 100.")
else:
	years_to_100=int(100-age)
	target_year=str(current_year+years_to_100)
	i=int(input("Please enter how many times the message should be printed: "))
	print(i*("You will reach the age of 100 in " + target_year + ".\n"))
