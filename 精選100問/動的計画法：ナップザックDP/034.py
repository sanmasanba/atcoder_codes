#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

@lru_cache
def func(N):
    if N == 0 or N == 1:
        return 1
    return func(N-1) + func(N-2)
     
#main
def main():
    N = int(input())
    print(func(N))

if __name__ == '__main__':
    main()