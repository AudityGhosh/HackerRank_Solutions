#!/bin/python3

# Incorrect Regex Challenge Solution
# problem link: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Author: Audity Ghosh
# Date: 30 December 2024
# Description:
# This script takes multiple test cases where each test case contains a string. 
# It checks if the string is a valid regular expression (regex) or not.
# If it's a valid regex, print "True", otherwise print "False".

# Importing the regex library
import re 

# Read the number of test cases
T = input()  # Number of test cases

# Loop through each test case
for i in range(int(T)):
    S = input()  # Read the regex string for the test case
    
    try:
        # Try to compile the regex string using re.compile()
        pattern = re.compile(S)
        print("True")  # If no error occurs, it's a valid regex
    except re.error:
        # If a re.error is raised, it's an invalid regex
        print("False")
