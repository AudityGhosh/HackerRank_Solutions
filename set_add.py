#!/bin/python3

# Set .add() Challenge Solution
# problem link: https://www.hackerrank.com/challenges/py-set-add/problem
# Author: Audity Ghosh
# Date: 21 January 2020
# Description:
# This script helps Rupal count the total number of distinct country stamps
# in her collection. The task is to find the total number of distinct
# country stamps after applying the .add() operation on a set.

# Read the total number of country stamps
t=int(input())  # The total number of country stamps

# Initialize an empty list to store the country names
data=[]

# Loop through each input country name
for i in range(t):
    k=input()  # Read the name of the country where the stamp is from
    data.append(k)  # Add the country name to the list

# Convert the list to a set to remove duplicates
s=set(data) 

# Convert the set back to a list to count the distinct country stamps
l=list(s)

# Print the total number of distinct country stamps
print(len(l))  # Output the length of the set (distinct countries)
