#!/usr/bin/python3
'''calculate perimeter'''

def island_perimeter(grid):
    '''calculate perimeter'''
    length = len(grid)
    width = 0
    height = 0
    next = 0
    prev = 0
    for row in range(0, length):
        for col in range(0, len(grid[row])):
            if grid[row][col] == 1:
                #check if next and prev col == 1
                try:
                    prev = grid[row][col-1]
                except IndexError:
                    pass
                try:
                    next = grid[row][col+1]
                except IndexError:
                    pass
                #check for height
                try:
                    top = grid[row-1][col]
                except IndexError:
                    pass
                try:
                    bott = grid[row+1][col]
                except IndexError:
                    pass
                if top ==1 and bott == 1 and prev ==1 and next ==1:
                    continue
                if top == 1 or bott == 1:
                    height += 1
                if prev == 1 or next == 1:
                    width += 1
    return (height) + (width    )

