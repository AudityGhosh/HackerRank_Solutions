#!/bin/python3

# Python: Division Challenge Solution
# Author: Audity Ghosh
# Date: 21 March, 2021
# Description:
# This script performs integer and float division for two input integers.

# Read two integers from standard input
a = int(input())
b = int(input())

# Ensure divisor is not zero
if b != 0:
    # Perform and print the results of divisions
    print(a // b)  # Integer division
    print(a / b)   # Float division
else:
    print("Division by zero is not allowed.")  # Handle zero divisor case
