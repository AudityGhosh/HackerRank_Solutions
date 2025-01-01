
#!/bin/python3

# Python String Find Substring Challenge Solution
# Author: Audity Ghosh
# Date: 20 March, 2020
# Description:
# This script takes an input string and a substring. It counts how many times the
# substring occurs within the string and prints the result. The traversal is done
# from left to right, and the search is case-sensitive.

# Function to count the number of occurrences of the substring in the string
def count_substring(string, sub_string):
    results = 0  # Initialize the counter for the substring occurrences
    sub_len = len(sub_string)  # Get the length of the substring
    
    # Loop through the string to check for occurrences of the substring
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:  # Check if the substring matches
            results += 1  # Increment the count if a match is found

    return results  # Return the total count