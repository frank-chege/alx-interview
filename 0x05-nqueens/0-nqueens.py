#!/usr/bin/python3
'''solving the n-quuens problem'''
import sys

# check if the correct argument is passed to the program
if len(sys.argv) != 2:
    sys.stdout.write('Usage: nqueens N\n')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    sys.stdout.write('N must be a number\n')
    sys.exit(1)

if n < 4:
    sys.stdout.write('N must be at least 4\n')
    sys.exit(1)

pos_list = []

for x in range(0, n, 2):
    for y in range(0, n, 2):
        pos_list.append([x, y])
print(pos_list)