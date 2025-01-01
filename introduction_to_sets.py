#!/bin/python3

# Python Sets Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Author: Audity Ghosh
# Date: 1 January 2025
# Description:
# This script calculates the average of all the plants with distinct heights in her greenhouse.

# Function to calculate the average of distinct heights
def average(array):
    p = set(array)  # Convert array to a set to remove duplicates
    sum = 0
    for i in p:  # Sum up all distinct heights
        sum = sum + i
    return (sum / len(p))  # Return average of distinct heights