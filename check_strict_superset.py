# Check Strict Superset Challenge Solution
# Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Author: Audity Ghosh
# Date: 1 January 2025
# Description:
# Given a set A and a number of other sets, we need to check if A is a strict superset of all the other sets.
# A set A is a strict superset of set B if:
# 1. All elements of B are in A, and
# 2. A has at least one element that is not in B.

a = set(map(int, input().split()))  # First line: Set A

t = int(input())  # Second line: Number of other sets

ans = 0  # Initial assumption: A is not a strict superset

# Iterate through each of the other sets
for i in range(t):
    b = set(map(int, input().split()))  # Read each set B
    
    all_el = True  # Flag to check if all elements of B are in A
    
    # Check if all elements of set B are in set A
    for el in b:
        if el not in a:
            all_el = False  # If any element of B is not in A, set the flag to False
            break  # No need to check further elements
    
    # If all elements are in A and B has fewer elements than A, A is a strict superset of B
    if all_el and len(b) < len(a):
        ans += 1  # Increment the counter if A is a strict superset of B

# If ans equals t, A is a strict superset of all other sets
if ans == t:
    print("True")
else:
    print("False")
