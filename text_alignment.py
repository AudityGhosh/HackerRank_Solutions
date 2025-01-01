#!/bin/python3

# Python String Alignment Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2020
# Description:
# This script generates the HackerRank Logo of variable thickness.
# The logo consists of a top cone, top pillars, middle belt, bottom pillars, and bottom cone.
# The thickness is an odd number and controls the size of the logo.

# Read the input thickness, which must be an odd number
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    # Align the characters and print the top cone of the logo
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # Center-align the pillars to form the top portion of the logo
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Center-align the middle belt
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # Center-align the bottom pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # Align the characters and print the bottom cone of the logo
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
