#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/3
"""

# Imports
import sys
import os
import re
from collections import Counter 

# Global variables
task="d-3"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
   
    xmax = 0
    ymax = 0
    claims = []
    # Init matrix and claims
    for row in rows:
        # ['1', '1', '3', '4', '4']
        # ['id', 'xstart', 'ystart', 'x', 'y']
        m = re.findall(r'\d+', row)
        claim = [int(i) for i in m] 
        claims.append(claim) 
        x = claim[1] + claim[3]
        y = claim[2] + claim[4]
        if x > xmax:
            xmax = x 
        if y > ymax:
            ymax = y 
    
    print("%d, %d" % (xmax, ymax))

    # Mark inches claimed with id's 
    matrix = [[[] for x in range(xmax+1)] for y in range(ymax+1)] 
    for claim in claims:
        for x in range(claim[1], claim[1] + claim[3]):
            for y in range(claim[2], claim[2] + claim[4]):
                matrix[x][y].append(claim[0]) 

    overlap = 0
    overlap_ids = set()
    non_overlap_id = set()

    # Find duplicate/single inch claims
    for x in range(xmax):
        for y in range(ymax):
            # a)
            if len(matrix[x][y]) > 1:
                overlap += 1
                overlap_ids.update(matrix[x][y])
            # b)
            if len(matrix[x][y]) == 1:
                non_overlap_id.update(matrix[x][y])
    
    # Find claim id that isn't overlapping
    non_overlap = non_overlap_id.difference(overlap_ids)

    print("A): %d" % (overlap))
    print(non_overlap)


# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)