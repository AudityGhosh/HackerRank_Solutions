#!/bin/python3

# HackerRank Finding the Percentage Challenge Solution
# Problem link: https://www.hackerrank.com/challenges/finding-the-percentage/problem 
# Author: Audity Ghosh
# Date: 4 January 2021
# Description:
# This script calculates and prints the average score of a student specified by the query_name, 
# rounded to 2 decimal places.

if __name__ == '__main__':
    # Read the number of students' records
    n = int(input())

    # Initialize an empty dictionary to store students' marks
    student_marks = {}

    # Read each student's name and their corresponding marks
    for _ in range(n):
        name, *line = input().split()  # Read the name and marks
        scores = list(map(float, line))  # Convert the marks to floats
        student_marks[name] = scores  # Store the name and marks in the dictionary

    # Read the query_name to get the student's marks to query
    query_name = input()

    # Calculate the sum of the scores for the queried student
    sum_score_of_the_student = 0
    for value in student_marks[query_name]:
        sum_score_of_the_student += value  # Add each score to the sum

    # Calculate the average score
    avg = float(sum_score_of_the_student / len(student_marks[query_name]))

    # Print the average score rounded to 2 decimal places
    print("%.2f" % round(avg, 2))
