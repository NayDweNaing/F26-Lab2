# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 28/9/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py


import sys #importing sys module to use command line arguments
name = sys.argv[1]; #taking the first command line argument as the name
age = sys.argv[2]; #taking the second command line argument as the age


#print a message that includes the name, age, and the number of command line arguments received.
print("Hi {}! Your age is {} and the system received {} arguments.".format(name, age, len(sys.argv)))