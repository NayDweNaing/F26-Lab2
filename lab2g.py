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

if status == "single":
    if income > 32000:
        print("Your tax is {}".format ( 3200 + (income - 32000)*high_tr));
    elif income <= 32000:
        print("Your tax is {}".format (income*low_tr));
    else:
        print("Please fill in your income correctly.");
elif status == "married":
    if income > 64000:
        print("Your tax is {}".format ( 6400 + (income-64000)*high_tr));
    elif income <= 64000:
        print("Your tax is {}".format (income*low_tr));
    else:
        print("Please fill in your income correctly.")
else:
    print("Please fill in the marital status correctly")


    