# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys

num_args = len(sys.argv) - 1

if num_args == 0:
    print("This script requires exactly two arguments. No arguments were provided!")
elif num_args == 2:
    print("Hello user, good job, your provided two arguments!")
else:
    number_words = {1: "one", 3: "three", 4: "four", 5: "five"}
    word = number_words.get(num_args, str(num_args))
    print("This script requires exactly two arguments. You provided {} arguments.".format(word))