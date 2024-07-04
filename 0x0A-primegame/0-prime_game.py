#!/usr/bin/python3
'''find the winner of a primegame'''

def is_prime(number):
    '''check if a no. is prime'''
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
    


def isWinner(x, nums):
    '''primegame winner'''
    #get all prime no.s from the list and store them in a diff list
    #take turns until all rounds are done to remove no.s starting with maria
    #to remove prime no, check if the no is in the prime list
    #if not in list, move to next player
    #if in list
    #remove the multiples of the no too
    #increment each player's score respectively
    prime = []
    maria = True
    maria_score = 0
    ben_score = 0
    ben = False
    for num in nums:
        if is_prime(num):
            prime.append
    for round in range(x):
        for number in nums:
            #create a list of int in range of the current integer
            lis = [num for num in range(1, number)]
            for num in lis:
                if is_prime(num):
                    #remove the prime no.
                    lis.remove(num)
                    #remove its multiples
                    for n in lis:
                        if n % num == 0:
                            lis.remove(n)
                    if maria:
                        maria_score += 1
                        maria = False
                    else:
                        ben_score += 1
                        maria = True

    if maria_score > ben_score:
        winner = 'Maria'
    elif ben_score > maria_score:
        winner = 'Ben'
    else:
        winner = None
    return winner

    