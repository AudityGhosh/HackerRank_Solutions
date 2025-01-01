#!/bin/python3

# Set .symmetric_difference() Operation Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Author: Audity Ghosh
# Date: 30 January 2020
# Description:
# This script calculates the total number of students who have subscribed to either
# the English or the French newspaper but not both using the set .symmetric_difference() operation.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())  # Read number of students who subscribed to the English newspaper
data1 = set(list(map(int, input().split(' '))))  # Roll numbers of students subscribed to English newspaper
t = int(input())  # Read number of students who subscribed to the French newspaper
data2 = set(list(map(int, input().split(' '))))  # Roll numbers of students subscribed to French newspaper

# Find the symmetric difference between the English and French subscription sets (students subscribed to either but not both)
s = set(data1.symmetric_difference(data2))

# Output the total number of students who have subscriptions to either the English or the French newspaper but not both
print(len(s))
