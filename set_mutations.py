#!/bin/python3

# Set Mutations Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Author: Audity Ghosh
# Date: 30 December 2025
# Description:
# This script performs set mutations based on operations like intersection_update, 
# difference_update, symmetric_difference_update, and update, then calculates the 
# sum of elements in the set after the mutations.

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())  # Read the number of elements in the set
a = set(map(int, input().split()))  # Read the elements of the set

n = int(input())  # Read the number of operations to perform on the set
for i in range(n):
    op, no_el = input().split()  # Read operation and number of elements in the other set
    no_el = int(no_el)  # Convert the number of elements to an integer
    
    b = set(map(int, input().split()))  # Read the elements of the other set

    # Perform the corresponding set mutation operation
    if op == "intersection_update":
        a.intersection_update(b)
    elif op == "difference_update":
        a.difference_update(b)
    elif op == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif op == "update":
        a.update(b)

# Output the sum of elements in the set after all mutations
print(sum(a))
