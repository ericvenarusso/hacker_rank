#!/usr/bin/python

def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_region = list(range(s, t + 1, 1))
    apples_near_house = 0
    oranges_near_house = 0
    fruits_near_house = []
    
    for i_apple in apples:
        if (a + i_apple) in house_region:
            apples_near_house+=1
            
    print(apples_near_house)
    
    for i_orange in oranges:
        if (b + i_orange) in house_region:
            oranges_near_house+=1
            
    print(oranges_near_house)
    
countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
