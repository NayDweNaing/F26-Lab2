
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user

str1 = input("Give me a sentence: ")
str2 = input("Give me another sentence: ")

if len(str1) == len(str2):
    print("Both sentences have the same characters!");
elif len(str1) > len(str2):
    print("The first sentence is longer than the second sentence.");
else:
    print("The second sentence is longer than the first sentence.");
    

