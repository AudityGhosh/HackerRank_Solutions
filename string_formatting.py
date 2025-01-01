#!/bin/python3

# Python String Formatting Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2020
# Description:
# This function prints the decimal, octal, hexadecimal, and binary values 
# for each integer from 1 to the given integer n.
# Each value is space-padded to match the width of the binary value of n.

# Function to print formatted values
def print_formatted(n):
    # Calculate the width needed for the binary representation of n
    l = len(str(bin(n))[2:])

    # Iterate through all integers from 1 to n
    for i in range(1, n + 1):
        # Print the decimal, octal, hexadecimal, and binary representations
        # Each value is right-aligned with padding to match the width of the binary value
        print(str(i).rjust(l, ' '),            # Decimal value, right-aligned
              oct(i)[2:].rjust(l, ' '),        # Octal value, right-aligned
              hex(i).upper()[2:].rjust(l, ' '), # Hexadecimal value (uppercase), right-aligned
              bin(i)[2:].rjust(l, ' '))         # Binary value, right-aligned
