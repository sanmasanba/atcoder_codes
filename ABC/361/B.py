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
    a, b, c, d, e, f = map(int, input().split(' '))
    g, h, i, j, k, l = map(int, input().split(' '))

    W = 1 if max(a, g) < min(j, d) else 0
    H = 1 if max(b, h) < min(e, k) else 0
    T = 1 if max(c, i) < min(l, f) else 0

    print('Yes' if W*H*T else 'No')

if __name__ == '__main__':
    main()