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
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # i = 1, 2, ..., N
    m = 0
    i = 1
    for i in range(1, N+1):
        day = A[m] - i
        print(day)
        # 当日に花火が揚がるようになったら、リストを進める
        if day == 0:
            i = A[m]
            m += 1

if __name__ == '__main__':
    main()