# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys
name = sys.argv[1];
age = sys.argv[2];

print("Hi {}! Yourage is {} and the system received {} arguments.".format(name, age, len(sys.argv)))