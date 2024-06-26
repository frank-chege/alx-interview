#!/usr/bin/python3
'''calculate perimeter'''

def island_perimeter(grid):
    '''calculate perimeter'''
    length = len(grid)
    width = 0
    height = 0
    first = False
    for row in range(0, length):
        for col in range(0, len(grid[row])):
            if grid[row][col] == 1 and first is False:
                #check for the first instance of 1
                width += 1
                height += 1
                first = True
            #check if next col is 1
            if first:
                count = 0
                try:
                    next_w = grid[row][col+1]
                    if next_w == 1:
                        #this row has the width
                        while True:
                            try:
                                #get width
                                next = grid[row][col+count]
                                if next == 1:
                                    width += 1
                                else:
                                    #get height
                                    count = 0
                                    while True:
                                        try:
                                            next = grid[row+count][col]
                                            if next == 1:
                                                height += 1
                                            else:
                                                return (height*2) + (width*2)
                                        except KeyError:
                                            return (height*2) + (width*2)
                                        count += 1
                                    
                            except KeyError:
                                #get height
                                count = 0
                                while True:
                                    try:
                                        next = grid[row+count][col]
                                        if next == 1:
                                            height += 1
                                        else:
                                            return (height*2) + (width*2)
                                    except KeyError:
                                        return (height*2) + (width*2)
                                    count += 1
                            count += 1
                    else:
                        #get height
                        while True:
                            try:
                                next = grid[row+count][col]
                                if next == 1:
                                    height += 1
                                else:
                                    count = 1
                                    while True:
                                        try:
                                            next = grid[row][col+count]
                                            if next == 1:
                                                width += 1
                                            else:
                                                return (height*2) + (width*2)
                                        except KeyError:
                                            return (height*2) + (width*2)
                                        count += 1
                                    
                            except KeyError:
                                count = 0
                                while True:
                                    try:
                                        next = grid[row][col+count]
                                        if next == 1:
                                            width += 1
                                        else:
                                            return (height*2) + (width*2)
                                    except KeyError:
                                        return (height*2) + (width*2)
                                    count += 1
                            count += 1
                except KeyError:
                    #this row has the height
                    while True:
                        try:
                            next = grid[row+count][col]
                            if next == 1:
                                height += 1

                            else:
                                count = 1
                                while True:
                                    try:
                                        next = grid[row+count][col-count]
                                        if next == 1:
                                            width += 1
                                        else:
                                            return (height*2) + (width*2)
                                    except KeyError:
                                        return (height*2) + (width*2)
                                    count += 1
                        except KeyError:
                            count = 0
                            while True:
                                try:
                                    next = grid[row+count][col-count]
                                    if next == 1:
                                        width += 1
                                    else:
                                        return (height*2) + (width*2)
                                except KeyError:
                                    return (height*2) + (width*2)
                                count += 1
                        count += 1