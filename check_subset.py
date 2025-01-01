# Check Subset Challenge Solution
# Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# Author: Audity Ghosh
# Date: 1 January 2025
# Description:
# Given two sets, we need to check whether the first set is a subset of the second set.
# The task is to print True if the first set is a subset of the second, and False otherwise.

# Read input from STDIN
t = int(input())  # Read the number of test cases

for i in range(t):
    n = int(input())  # Read the number of elements in the first set
    s = set(map(int, input().split()))  # Read the elements of the first set
    m = int(input())  # Read the number of elements in the second set
    r = set(map(int, input().split()))  # Read the elements of the second set

    # Check if the first set is a subset of the second set
    print(s.issubset(r))  # Output True if s is a subset of r, otherwise False
