
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 28/9/2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py


str1 = input("Give me a sentence: ") #request the first sentence from user
str2 = input("Give me another sentence: ") #request the second sentence from user

if len(str1) == len(str2): #check if the length of both sentences are equal
    print("Both sentences have the same characters!"); #then print that they are equal
elif len(str1) > len(str2): #if the first sentence is longer than the second sentence, print that the first sentence is longer
    print("The first sentence is longer than the second sentence.");
else: #if the second sentence is longer than the first sentence, print that the second sentence is longer
    print("The second sentence is longer than the first sentence.");
    

