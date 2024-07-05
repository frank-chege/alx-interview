#!/usr/bin/python3

def is_prime(number):
    '''Check if a number is prime'''
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

def generate_prime_list(n):
    '''Generate a list of prime numbers up to n'''
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def play_game(n, primes):
    '''Play one round of the game'''
    set_numbers = set(range(1, n + 1))
    turn = 0  # Maria starts (0: Maria, 1: Ben)

    while True:
        possible_moves = [p for p in primes if p in set_numbers]
        if not possible_moves:
            return turn  # Return the current turn as the loser

        prime = possible_moves[0]
        multiples = {prime * k for k in range(1, (n // prime) + 1)}
        set_numbers -= multiples
        turn = 1 - turn  # Switch turns

def isWinner(x, nums):
    '''Determine the winner after x rounds'''
    maria_score = 0
    ben_score = 0
    max_n = max(nums)
    primes = generate_prime_list(max_n)

    for n in nums:
        loser = play_game(n, primes)
        if loser == 1:  # Ben loses, so Maria wins
            maria_score += 1
        else:  # Maria loses, so Ben wins
            ben_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None

# Example usage
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output should be 'Ben'
