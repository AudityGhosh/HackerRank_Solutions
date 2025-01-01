# HackerRank Challenge: sWAP cASE
# Author: Audity Ghosh
# Date: 24 March, 2021
# Description:
# This function takes a string and swaps its case (lowercase to uppercase and vice versa).

def swap_case(s):
    # Use the built-in string method swapcase() to swap cases
    return s.swapcase()

# Read input string
s = input()

# Call the function and print the result
print(swap_case(s))
