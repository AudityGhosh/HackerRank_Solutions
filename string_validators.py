#!/bin/python3

# Python String Validators Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2020
# Description:
# This script checks whether a given string contains any alphanumeric characters, 
# alphabetical characters, digits, lowercase characters, and uppercase characters.
# It prints the result for each condition (True or False).

# Read the input string
s = input().strip()

# Initialize counters for each condition
an = 0  # Alphanumeric characters
ab = 0  # Alphabetical characters
d = 0   # Digits
l = 0   # Lowercase characters
u = 0   # Uppercase characters

# Loop through each character in the string
for i in s:
    if i.isalpha():  # Check if character is alphabetical
        ab += 1
    if i.isalnum():  # Check if character is alphanumeric
        an += 1
    if i.isdigit():  # Check if character is a digit
        d += 1
    if i.islower():  # Check if character is lowercase
        l += 1
    if i.isupper():  # Check if character is uppercase
        u += 1

# Print the result for each validation
print("True" if an > 0 else "False")  # Alphanumeric
print("True" if ab > 0 else "False")  # Alphabetical
print("True" if d > 0 else "False")   # Digits
print("True" if l > 0 else "False")   # Lowercase
print("True" if u > 0 else "False")   # Uppercase
