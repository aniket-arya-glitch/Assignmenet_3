#Calculate Factorial Using a Function

a = int(input('Enter a number:'))


def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)


result = factorial(a)
print('Factorial of', a, 'is=', result)





#Using the Math Module for Calculations

a = int(input('Enter a number:'))
from math import *

square_root = sqrt(a)
logarithm = log(a, e)
sine = sin(a)
print('Square root:', square_root)
print('logarithm :', logarithm)
print('Sine:', sine)
