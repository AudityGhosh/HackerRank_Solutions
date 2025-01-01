#!/bin/python3

# Set .intersection() Operation Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Author: Audity Ghosh
# Date: 30 January 2020
# Description:
# This script calculates the total number of students who have subscribed to both
# the English and French newspapers using the set .intersection() operation.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  # Read number of students who subscribed to English newspaper
data1 = set(list(map(int, input().split(' '))))  # Roll numbers of students subscribed to English newspaper
t = int(input())  # Read number of students who subscribed to French newspaper
data2 = set(list(map(int, input().split(' '))))  # Roll numbers of students subscribed to French newspaper

# Find the intersection of both sets (students subscribed to both newspapers)
s = set(data1.intersection(data2))

# Output the total number of students who have subscriptions to both newspapers
print(len(s))
