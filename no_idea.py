#!/bin/python3

# Python Sets Challenge Solution
# problem link: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Author: Audity Ghosh
# Date: 1 January 2025
# Description:
# This script calculates the total happiness based on an array of integers and two disjoint sets.
# You like all the integers in set A and dislike all the integers in set B. 
# Your happiness starts at 0 and for each integer in the array:
# - If the integer is in set A, you gain 1 unit of happiness.
# - If the integer is in set B, you lose 1 unit of happiness.
# The final happiness value is printed at the end.

# Read the input values: n (size of array), m (size of sets a and b)
n, m = map(int, input().split())

# Read the array of integers
arr = list(map(int, input().split()))

# Read the two sets of integers (a and b)
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# Initialize happiness variable
happiness = 0

# Iterate over the array and calculate happiness based on the sets
for el in arr:
    if el in a:      # If element is in set a, add 1 to happiness
        happiness += 1
    if el in b:      # If element is in set b, subtract 1 from happiness
        happiness -= 1

# Output the final happiness
print(happiness)
