#!/bin/python3

# Python Alphabet Rangoli Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2021
# Description:
# This function prints an alphabet rangoli of a given size.
# The rangoli consists of rows of alphabets arranged in a symmetrical pattern
# with the first row containing the largest alphabet and each subsequent row
# decreasing in size, forming a mirror image.

# Function to print the rangoli pattern
def print_rangoli(n):
    # Initialize a list to hold the rows of the rangoli pattern
    data = []
    
    # Loop to create the upper half (including the middle row) of the rangoli
    for i in range(1, n + 1):
        # String to build each row
        s = ""
        
        # Add dashes for padding before the alphabets
        s += "-" * (2 * (n - i))
        
        # Add the alphabets in decreasing order from the center (left part)
        for j in range(n, n - i, -1):
            s += chr(ord('a') + j - 1) + "-"
        
        # Remove the last dash
        s = s[:-1]
        
        # Store the current row in the list
        t = s
        
        # Reverse the string and remove the first character to form the right part of the row
        s = s[::-1]
        s = s[1:]
        
        # Complete the row by combining the left and right parts
        data.append(t + s)
        
        # Print the current row
        print(t + s)
    
    # Reverse the list to print the lower half (excluding the middle row)
    data.reverse()
    
    # Print the lower half of the rangoli
    for i in range(1, len(data)):
        print(data[i])

