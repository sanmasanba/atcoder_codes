#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    T = list(map(lambda x: int(x) - 1, input().split(' ')))
    teeth = [1 for _ in range(N)]

    for t in T:
        if teeth[t] == 1:
            teeth[t] = 0
        else:
            teeth[t] = 1

    print(sum(teeth))

if __name__ == '__main__':
    main()