#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
phrase = 'Last digit of'

if number[number.length-1] == 0:
    print('{0} {1} is {2} and is 0'.format(phrase, number, number[number.length-1]))
elif number[number.length-1] > 5:
    print('{0} {1} is {2} and is greater than 5'.format(phrase, number, number[number.length-1]))
else:
    print('{0} {1} is {2} and is less than 6 and not 0'.format(phrase, number, number[number.length-1]))

