#!/bin/python3

# Exceptions Challenge Solution
# problem link: https://www.hackerrank.com/challenges/exceptions/problem
# Author: Audity Ghosh
# Date: 23 January 2021
# Description:
# This script takes multiple test cases, for each test case performs integer division, 
# and handles ZeroDivisionError and ValueError exceptions by printing the respective error codes.

# Read the number of test cases
t = int(input())  # Read the number of test cases

# Loop through each test case
for i in range(0, t):
    try:
        # Read the input values and convert them into integers
        a, b = map(int, input().split(' '))
        # Perform integer division and print the result
        print(a // b)
    except ZeroDivisionError as e:
        # Handle division by zero and print the error code
        print("Error Code: integer division or modulo by zero")
    except ValueError as p:
        # Handle invalid integer input and print the error code
        print(f'Error Code: {p}')
