# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 28/9/2026
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py


#request a pin number from user and convert it to integer
pin = int(input("Please put your pin number: ")); 
while pin != 1234: #if pin is not equal to 1234,
    print("Please try again") #print "Please try again"
    pin = int(input("Please put your pin number: ")) #then request the pin number from user again
print("Success") #if the pin is equal to 1234, print "Success"
