#
"""
Title: Halloween Sale
Link: https://www.hackerrank.com/challenges/halloween-sale/problem
"""

#!/usr/bin/python

def howManyGames(p, d, m, s):
    price_list = []
    
    while sum(price_list) < s:
        
        if p <= m:
            price_list.append(m)
        else:
            price_list.append(p)
            p -= d
        
    if sum(price_list) > s:
        return len(price_list) - 1
    else:
        return len(price_list)
    
howManyGames(76, 90, 3, 4000)
