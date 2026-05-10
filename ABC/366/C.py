#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    Q = int(input())
    QUERY = [input() for _ in range(Q)]
    balls = {}

    for qx in QUERY:
        try:
            q, x = map(int, qx.split(' '))
        except:
            q = int(qx)
        if q == 1:
            if x not in balls:
                balls[x] = 0
            balls[x] += 1
        if q == 2:
            balls[x] -= 1
            if balls[x] == 0:
                del balls[x]
        if q == 3:
            print(len(balls))

if __name__ == '__main__':
    main()