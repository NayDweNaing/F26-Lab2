# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

import math

number = int(input("Please type in a number: "));
while number != 0:
    print(math.sqrt(number))
    number = int(input("Please type in a number: "))
print("Exiting...");


