# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

import math #importing math module to use the sqrt function

number = int(input("Please type in a number: ")); #taking the first input from the user and converting it to an integer
while number != 0: 
    print(math.sqrt(number)) #if the number is not zero, print the square root of the number
    number = int(input("Please type in a number: ")) #then request another number from the user
print("Exiting..."); #if the user inputs 0, the loop will exit and print "Exiting..."


