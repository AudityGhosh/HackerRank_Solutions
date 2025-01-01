#!/bin/python3

# Symmetric Difference Challenge Solution
# problem link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Author: Audity Ghosh
# Date: 21 January 2020
# Description:
# This script takes two sets of integers, calculates their symmetric difference,
# and prints the result in ascending order.

# Read the size of the first set
n = int(input())  # Read the size of set A
datap = list(map(int, input().split(' ')))  # Read the space-separated integers for set A

# Read the size of the second set
m = int(input())  # Read the size of set B
datal = list(map(int, input().split(' ')))  # Read the space-separated integers for set B

# Convert the lists into sets
data1 = set(datap)  # Create set A
data2 = set(datal)  # Create set B

# Calculate the symmetric difference by performing union and intersection operations
o = set(data1.union(data2))  # Union of both sets
u = set(data1.intersection(data2))  # Intersection of both sets
l = set(o.difference(u))  # Symmetric difference: union minus intersection

# Convert the symmetric difference to a sorted list and print the result
k = list(l)  # Convert the set to a list
k.sort()  # Sort the list in ascending order
for i in k:
    print(i)  # Print each element of the sorted symmetric difference
