# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: use for loop.
# Usage: ./lab2k.py

### lab2k.py
#Write a Python program that calculates the sum of all even numbers from 1 to 100 (inclusive).
#- Use a for loop to iterate over the range of numbers from 1 to 100.
#- Inside the loop, check if the current number is even.
#- If the number is even, add it to a running total.
#- After the loop, print the final sum.
total = 0;

for i in range(1, 101):  # Loop through numbers from 1 to 100
    if i % 2 == 0:  # Check if the number is even
        total += i  # Add the even number to the total
print("The sum of all even numbers from 1 to 100 is:", total)  # Print the final sum


