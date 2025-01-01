#!/bin/python3

# Python String Mutation Challenge Solution
# Author: Audity Ghosh
# Date: 28 March, 2021
# Description:
# This script takes an immutable string and modifies it by replacing
# the character at a given index with a new character. It then prints
# the modified string.

# Function to mutate the string
def mutate_string(string, position, character):
    # Slicing the string and inserting the character at the specified position
    return string[:position] + character + string[position+1:]