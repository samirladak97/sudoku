# A simple python file that accepts user inputs
# Users can either input numbers during command or input them after when prompted
# If they input in command we can add as many numbers as the user wants
# If they input after, we just ask for 2 numbers

import math
import sys

def simpleAdd(num1, num2):
    result = num1 + num2
    return result

if __name__ == "__main__":
    # Read user input
    # If numbers are provided in command then add sum
    if len(sys.argv) > 1:
        sum = 0
        for x in range(1, len(sys.argv)):
            sum += int(sys.argv[x])
        """
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        sum = simpleAdd(num1, num2)
        """
        print("The sum is: " + str(sum))
    # if numbers not provided, ask for them
    else:
        print("Let's calculate your sum!")
        num1 = int(input("What is the first number: "))
        num2 = int(input("What is the second number: "))
        sum = simpleAdd(num1, num2)
        print("The sum is: " + str(sum))
     