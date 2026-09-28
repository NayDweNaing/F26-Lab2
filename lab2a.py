# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 28/9/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

x = int(input("Give me a number: ")) #request a number from user and convert it to interger

print(type(x)) #print the type of x

if x > 6: #if x is greater than 6, print "Yeah, it's greater than 6"
    print("Yeah, it's greater than 6")
else: #if x is not greater than 6, print "It's not greater than 6"
    print("It's not greater than 6")

if 4 <= x < 12: #if x is between or equal to 4 and less than 12, print "It's between or equal to 4 and less than 12"
    print("It's between or equal to 4 and less than 12")
else: #if x is not between or equal to 4 and less than 12, print "It's not within 4 and 12"
    print("It's not within 4 and 12")

