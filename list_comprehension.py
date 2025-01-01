#!/bin/python3

# HackerRank List Comprehensions Challenge Solution
# problem link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Author: Audity Ghosh
# Date: 1 January 2021
# Description:
# This script generates all possible coordinates on a 3D grid given three integer dimensions (x, y, z),
# and an integer (n). It filters out the coordinates where the sum of x, y, and z equals n.
# The solution uses list comprehensions to generate the valid coordinates.

if __name__ == '__main__':
    # Read input values: x, y, z (dimensions of the cuboid) and n (sum to exclude)
    x = int(input())  # Length dimension
    y = int(input())  # Width dimension
    z = int(input())  # Height dimension
    n = int(input())  # The sum to exclude from the coordinates

    # Generate and filter coordinates using list comprehension
    data_final = [
        [i, j, k]  # Coordinate [i, j, k]
        for i in range(x + 1)  # Loop through x-dimension (0 to x)
        for j in range(y + 1)  # Loop through y-dimension (0 to y)
        for k in range(z + 1)  # Loop through z-dimension (0 to z)
        if i + j + k != n  # Include only those where the sum is not equal to n
    ]

    # Output the resulting list of valid coordinates
    print(data_final)
