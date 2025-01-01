#!/bin/python3

# Set .union() Operation Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-union/problem
# Author: Audity Ghosh
# Date: 21 January 2020
# Description:
# This script calculates the total number of students who have subscribed to 
# at least one of the English or French newspapers using the set .union() operation.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
data1=list(map(int, input().split(' ')))
m=int(input())
data2=list(map(int, input().split(' ')))
s=set(data1)
k=set(data2)
o=set(s.union(k))
l=list(o)
print(len(l))
