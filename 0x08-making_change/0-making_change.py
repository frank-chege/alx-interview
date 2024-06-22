#!/usr/bin/python3
'''making change'''

def makeChange(coins: list[int], total: int)->int:
    '''get the minimum no. of coins required to achieve the total'''
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    sum = 0
    count = 0
    length = len(coins)
    for idx in range(0, length):
        while sum <= total:
            count += 1
            sum += coins[idx]
            if sum == total:
                return count
        #remove last count and sum
        count -= 1
        sum -= coins[idx]
    return -1
        