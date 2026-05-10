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
    N = int(input())
    for i in range(N+1):
        for j in range(N-i+1):
            for k in range(N-i-j+1):
                print(i, j, k)

if __name__ == '__main__':
    main()