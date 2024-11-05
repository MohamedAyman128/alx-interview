#!/usr/bin/python3
"""n queens problem set"""
import sys


def check_input():
    """this check if the input is correct"""
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        args[1] = int(args[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if args[1] < 4:
        print("N must be at least 4")
        exit(1)


def set_queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from set_queens(n, i + 1,
                                      a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in set_queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


if __name__ == "__main__":
    check_input()
    solve(sys.argv[1])