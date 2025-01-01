#!/bin/python3

# Python Capitalize Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2021
# Description:
# This function capitalizes the first letter of each word in the given full name.
# The first and last names, as well as any other words in the string, should have their
# first letter capitalized while keeping the rest of the letters in lowercase.

# Complete the solve function below.
def solve(s):
    # Iterate through each word in the string
    for word in s.split():
        # Replace the word with its capitalized version
        s = s.replace(word, word.capitalize())
    return s  # Return the updated string with capitalized words