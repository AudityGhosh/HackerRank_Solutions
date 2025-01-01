#!/bin/python3

# HackerRank Nested Lists Challenge Solution
# problem link: https://www.hackerrank.com/challenges/nested-list/problem
# Author: Audity Ghosh
# Date: 3 January 2021
# Description:
# This script finds the name(s) of the student(s) who have the second lowest grade.
# The names are printed alphabetically if there are multiple students with the second lowest grade.

if __name__ == '__main__':
    # Initialize an empty list to store student name and score pairs
    students = []

    # Read the number of students
    for _ in range(int(input())):
        name = input()  # Read the student's name
        score = float(input())  # Read the student's score
        students.append([name, score])  # Append the name and score to the list

    # Find the second lowest score by sorting the unique scores and picking the second one
    second_score = sorted(list(set(x[1] for x in students)))[1]

    # Initialize an empty list to store the names of students with the second lowest score
    names = []

    # Iterate through the list of students and select those with the second lowest score
    for i, v in students:
        if v == second_score:
            names.append(i)  # Append the name to the names list

    # Sort the names alphabetically
    names.sort()

    # Print each name on a new line
    for i in names:
        print(i)
