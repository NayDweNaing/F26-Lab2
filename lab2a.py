# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
x = int(input("Give me a number: "))

print(type(x))

if x > 6:
    print("Yeah, it's greater than 6")
else:
    print("It's not greater than 6")

if 4 <= x < 12:
    print("It's between or equal to 4 and less than 12")
else:
    print("It's not within 4 and 12")

