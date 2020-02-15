#! /usr/bin/env python
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

Modulus operator
Conditional statements
Checking for equality
'''

# Functions can be imported into other programs
def is_even(n):
    if n%2 == 0:
        even = True
    else:
        even = False
    return even


def is_odd(n):
    if n%2 ==1:
        odd = True
    else:
        odd = False
    return odd


def main():
    n = int(input('Please enter a non-decimal number: '))
    m = int(input('Please enter a number to divide by: '))
    if is_even(n) == True:
        print (str(n) + " is an even number.")
    elif is_odd(n) == True:
        print (str(n) + " is na odd number.")
    else:
        print (str(n) + " is not a number.")

# n dividable by 4?
    if n%4 == 0:
        print (str(n) + " is perfectly dividable by 4.")

# n dividable by m
    if n%m == 0:
        print (str(n) + " divided by " + str(m) + " equals to " + str(int(n/m)) + ".")
    else:
        print (str(n) + "is not dividable by " + str(m) + ".")

# Only runs if run from the shell
if __name__ == '__main__':
    main()

