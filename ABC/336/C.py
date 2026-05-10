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
    n = int(input())
    res = ''
    N = n-1
    while N >= 1:
        res += str(N%5)
        N //= 5
    if n == 1:
        print(0)
    else:
        for i in res[::-1]:
            print(int(i)*2, end='')

if __name__ == '__main__':
    main()