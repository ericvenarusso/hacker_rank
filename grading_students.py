"""
Title: Grading Students
Link: https://www.hackerrank.com/challenges/grading/problem
"""

#!/usr/bin/python

def gradingStudents(grades):
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        else:
            multiples_of_5 = ((i // 5) * 5) + 5
            if (multiples_of_5 - i) < 3:
                new_grades.append(multiples_of_5)
            else:
                new_grades.append(i)
                
    return new_grades

gradingStudents([73, 67, 38, 33])
