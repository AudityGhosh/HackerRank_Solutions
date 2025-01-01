#!/bin/python3

# HackerRank Challenge: Print Function
# Author: Audity Ghosh
# Date: 23 March 2021
# Description:
# This script prints integers from 1 to `n` as a single string, without spaces.

# Read the integer input
n = int(input())

# Print numbers from 1 to n on the same line, without spaces
for i in range(1, n + 1):
    print(i, end="")
