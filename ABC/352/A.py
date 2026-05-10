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
    N, X, Y, Z = map(int, input().split(' '))
    
    up, low = max(X, Y), min(X, Y)

    if low <= Z <= up:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()