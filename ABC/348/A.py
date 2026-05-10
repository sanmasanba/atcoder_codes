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
    for i in range(N):
        print('o' if (i+1)%3 else 'x', end='')

if __name__ == '__main__':
    main()