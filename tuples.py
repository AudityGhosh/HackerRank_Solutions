#!/bin/python3

# Python Tuples Challenge Solution
# problem link: https://www.hackerrank.com/challenges/python-tuples/problem
# Author: Audity Ghosh
# Date: 21 January 2021
# Description:
# This script takes an integer n and a list of n space-separated integers, 
# creates a tuple from these integers, and prints the hash value of the tuple.

# Read the input values
n = int(input())  # Read the number of elements in the tuple
integer_list = tuple(map(int, input().split()))  # Read the space-separated integers and convert them into a tuple

# Print the hash value of the tuple
print(hash(integer_list))  # Output the hash of the tuple
