#!/usr/bin/env python3
"""
calculate the minimun copy and paste operations
required to obtain the specified no. of characters
"""

def minOperations(n):
    total = 0
    if n <= 1:
        return 0
    else:
        for x in range(n-1,0,-1):
            if n <= 1:
                break
            if n % x == 0:
                total += x
                n = n // x
        return total