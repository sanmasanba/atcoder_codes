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
    Q = deque()
    while 1:
        q = int(input())
        Q.append(q)
        if q == 0:
            break

    while Q:
        print(Q.pop())

if __name__ == '__main__':
    main()