# Recursive factorial calculator

import math
import sys

def factorial(x):
    x = int(x)
    if x <= 1:
        return 1
    else:
        return (x * factorial(x-1))

fac = input("Which number would you like to calculate the factorial for: ")
out = factorial(int(fac))

print(out)
