# The Captain's Room Challenge Solution
# Problem Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Author: Audity Ghosh
# Date: 31 December 2025
# Description:
# The task is to find the Captain's room number in a hotel where all families' rooms
# appear multiple times in the list except for the Captain's room number which appears only once.

# Read input from STDIN
t = int(input())  # Read the size of each family group
num = list(map(int, input().split()))  # Read the room numbers

# Create a dictionary to count the frequency of each room number
freq = {}

# Loop through the list of room numbers and count occurrences
for n in num:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

# Loop through the dictionary to find the room number that appears only once
for n in freq.keys():
    if freq[n] == 1:
        print(n)  # Output the Captain's room number
