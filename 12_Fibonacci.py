#! /usr/bin/env python
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

# def fibonacci(num):
#     a = 0
#     b = 1
#     fib = [1]
#     for n in range(num-1):
#         c = a+b
#         fib.append(c)
#         a = b
#         b = c
#     return fib
#
# if __name__ == '__main__':
#     num = int(input("Print how many Fibonacci numbers? "))
#     if num >= 1:
#         print(fibonacci(num))

## As a generator

def fibonacci():
    a = 0
    b = 1
    yield a + b

for i in range(20):
    num = next(fibonacci())
    print(num)
