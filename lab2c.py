
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

str1 = input("Give me a sentence: ") #request the first sentence from user
str2 = input("Give me another sentence: ") #request the second sentence from user

if len(str1) == len(str2): #check if the length of both sentences are equal
    print("Both sentences have the same characters!"); #then print that they are equal
elif len(str1) > len(str2): #if the first sentence is longer than the second sentence, print that the first sentence is longer
    print("The first sentence is longer than the second sentence.");
else: #if the second sentence is longer than the first sentence, print that the second sentence is longer
    print("The second sentence is longer than the first sentence.");
    

