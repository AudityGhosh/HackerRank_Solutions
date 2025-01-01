#!/bin/python3

# Python If-Else Challenge Solution
# Author: Audity Ghosh
# Date: 20 March, 2021
# Description:
# This script evaluates an integer input `n` and determines if it is "Weird" or "Not Weird"
# based on the given conditions.

n = int(input("Enter a number: ").strip())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
