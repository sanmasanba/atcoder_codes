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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    for a in A:
        if a%K == 0:
            print(a//K, end=' ')

if __name__ == '__main__':
    main()