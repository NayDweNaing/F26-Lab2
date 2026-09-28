# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 28/9/2026
# Purpose: use for loop.
# Usage: ./lab2k.py

total = 0;

for i in range(1, 101):  # Loop through numbers from 1 to 100
    if i % 2 == 0:  # Check if the number is even
        total += i  # Add the even number to the total
print("The sum of all even numbers from 1 to 100 is:", total)  # Print the final sum


