#!/bin/python3

# Python Designer Door Mat Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2020
# Description:
# This script generates a designer door mat pattern with specified dimensions.
# The mat consists of a central "WELCOME" and a pattern of | and - characters. 
# The mat size is determined by an odd integer input and is symmetric.

# Read the input dimensions (N and M)
N, M = input().split(" ")
list=[]
n = int(N)
m = int(M)
w = int((m - 3) / 2)

# Create the top half of the mat (including the middle "WELCOME" line)
for i in range(1, int(n / 2) + 1):
    string = "-" * w + ".|." * ((2 * i) - 1) + "-" * w  # Construct each line pattern
    print(string)  # Print the current line
    list.append(string)  # Store the line in the list
    w = w - 3  # Reduce the width for the next line

# Create the middle "WELCOME" line
p = int((m - 7) / 2)
print("-" * p + "WELCOME" + "-" * p)

# Print the bottom half of the mat (reverse of the top half)
list.reverse()  # Reverse the stored pattern
for i in list:
    print(i)
