"""
Title: Apple and Orange
Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

#!/usr/bin/python

def countApplesAndOranges(s, t, a, b, apples, oranges):

    def _count_near_fruits(tree_distance, fruits, fruits_near_house = 0):
        for i_fruit in fruits:
            fruit_distance = (tree_distance + i_fruit)
            
            if (fruit_distance >= s) and (fruit_distance  <= t):
                fruits_near_house+=1
                
        return fruits_near_house
            
 
    print(_count_near_fruits(a, apples))
    print(_count_near_fruits(b, oranges))
    
countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
