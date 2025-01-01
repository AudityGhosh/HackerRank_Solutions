#!/bin/python3

# Python Text Wrap Challenge Solution
# Author: Audity Ghosh
# Date: 30 March, 2020
# Description:
# This script wraps a given string into a paragraph of a specified width using the textwrap module.
# The string will be broken at the specified width, and newline characters will be added at the breaks.

import textwrap

def wrap(string, max_width):
    # Use the textwrap.fill method to wrap the string into the specified width
    return textwrap.fill(string, max_width)