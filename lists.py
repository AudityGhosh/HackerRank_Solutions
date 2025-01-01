#!/bin/python3

# Python Lists Challenge Solution
# problem link: https://www.hackerrank.com/challenges/python-lists/problem
# Author: Audity Ghosh
# Date: 20 January 2021
# Description:
# This script processes a series of commands to manipulate a list. The commands include inserting, 
# removing, appending elements, sorting, reversing, and printing the list. The program executes 
# each command in sequence and prints the list after the relevant "print" command.

# Initialize an empty list
data = []

# Read the number of commands
for _ in range(int(input())):
    # Read the command and its parameters
    instructions_with_values = list(map(str, input().split()))
    
    # Execute the corresponding operation based on the command
    if instructions_with_values[0] == "insert":
        data.insert(int(instructions_with_values[1]), int(instructions_with_values[2]))  # Insert at position
    elif instructions_with_values[0] == "reverse":
        data.reverse()  # Reverse the list
    elif instructions_with_values[0] == "remove":
        data.remove(int(instructions_with_values[1]))  # Remove first occurrence of element
    elif instructions_with_values[0] == "sort":
        data.sort()  # Sort the list
    elif instructions_with_values[0] == "append":
        data.append(int(instructions_with_values[1]))  # Append element to the end of the list
    elif instructions_with_values[0] == "pop":
        data.pop(-1)  # Pop the last element
    else:
        print(data)  # Print the list
