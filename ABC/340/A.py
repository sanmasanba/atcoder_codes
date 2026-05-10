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
    A, B, D = map(int, input().split(' '))
    res = A
    while 1:
        print(res, end=' ')
        res += D
        if res > B:
            break

if __name__ == '__main__':
    main()