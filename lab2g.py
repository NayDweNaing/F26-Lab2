# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

status = input("Please enter your marital status (single/married): ");
status = status.lower();
income = int(input("What's your income: "))
low_tr = 0.1;
high_tr = 0.25;

if status == "single": #if the user is single
    if income > 32000: #and earns over 32000,
        print("Your tax is {}".format ( 3200 + (income - 32000)*high_tr)); #they will have higher tax rate
    elif income <= 32000: #and earns less than or equal to 32000,
        print("Your tax is {}".format (income*low_tr)); #they will have lower tax rate
    else:
        print("Please fill in your income correctly."); #this will print if the user inputs a negative number or a non-integer value for income
elif status == "married": #if the user is married
    if income > 64000: #and earns over 64000,
        print("Your tax is {}".format ( 6400 + (income-64000)*high_tr)); #they will have higher tax rate
    elif income <= 64000: #and earns less than or equal to 64000,
        print("Your tax is {}".format (income*low_tr)); #they will have lower tax rate
    else:
        print("Please fill in your income correctly.") #this will print if the user inputs a negative number or a non-integer value for income
else:
    print("Please fill in the marital status correctly") #this will print if the user inputs a value different to provided status


    