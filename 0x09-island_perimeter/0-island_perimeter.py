#!/usr/bin/python3
'''Calculate perimeter of the island in the grid'''

def island_perimeter(grid):
    '''Calculate perimeter of the island in the grid'''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top neighbor
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left neighbor
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right neighbor
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
