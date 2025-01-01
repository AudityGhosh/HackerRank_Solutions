#!/bin/python3

# Set .discard(), .remove() & .pop() Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Author: Audity Ghosh
# Date: 21 January 2020
# Description:
# This script performs several set operations like .remove(), .discard(), and .pop() 
# on a set of integers and calculates the sum of the remaining elements in the set.

# Read the number of elements in the set
n=int(input())  # The total number of elements in the set

# Read the space-separated elements of the set and convert to a set
data=list(map(int, input().split(' ')))  # Read the elements of the set
s=set(data)  # Create a set from the list

# Read the number of operations to perform
t=int(input())  # The number of operations

# Loop through each operation
for i in range(t):
    m=list(input().split(' '))  # Read the operation and its associated value
    if m[0]=='remove':  # If the operation is remove
        s.remove(int(m[1]))  # Remove the element from the set
    elif m[0]=='discard':  # If the operation is discard
        s.discard(int(m[1]))  # Discard the element (no error if not found)
    elif m[0]=='pop':  # If the operation is pop
        s.pop()  # Pop an arbitrary element from the set

# Calculate the sum of the remaining elements in the set
sum=0
for i in s:
    sum+=i  # Sum up the remaining elements in the set

# Print the total sum of the elements in the set
print(sum)  # Output the sum of the elements
