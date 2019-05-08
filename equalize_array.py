"""
Title: Equalize the Array
Link: https://www.hackerrank.com/challenges/halloween-sale/problem
"""

#!/usr/bin/python

def equalizeArray(arr):
    most_frequent = max(set(arr), key = arr.count) 
    different_numbers = len([i for i in arr if i != most_frequent])
    
    return different_numbers
