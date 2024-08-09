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
    N = int(input())
    Q = [list(map(int, input().split(' '))) for _ in range(N)]
    
    MAP = [[0 for j in range(100)] for i in range(100)]
    for a, b, c, d in Q:
        for x in range(a, b):
            for y in range(c, d):
                MAP[x][y] = 1
    print(sum([sum(m) for m in MAP]))

if __name__ == '__main__':
    main()