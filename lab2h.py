#Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops.
# Usage: ./lab2h.py

# TO DO 1: 
# Creat variable timer.
# The value of timer should initially be 10.
# Use a while loop to create program that counts down from 10 with timer to 1.
# When you reach 1 end the loop and print blast off!

timer = 10; #set the time to 10
while timer != 0: #until the timer reaches 0, keep looping
    print(timer)
    timer = timer - 1 #if the timer is not zero it will keep subtracting 1 from the timer 
print("blast off!") #it will print blast off when the timer reaches 0

    
