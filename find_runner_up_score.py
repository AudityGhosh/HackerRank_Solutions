#!/bin/python3

# HackerRank Find the Runner-Up Score Challenge Solution
# problem link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Author: Audity Ghosh
# Date: 2 January 2021
# Description:
# This script finds the runner-up score from a list of scores.
# It first sorts the list of scores in descending order, then finds and prints
# the first score that is not the maximum (i.e., the runner-up score).

if __name__ == '__main__':
    # Read input values: n (number of participants) and arr (list of scores)
    n = int(input())  # Number of participants (not used directly)
    arr = list(map(int, input().split()))  # List of participant scores

    # Sort the list of scores in descending order
    arr.sort(reverse=True)

    # Iterate through the sorted list and find the first score that is not the maximum
    for i in arr:
        if(i is not max(arr)):  # If score is not the maximum score
            print(i)  # Print the runner-up score
            break  # Exit the loop after finding the runner-up score
