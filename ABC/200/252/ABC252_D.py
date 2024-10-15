#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

@lru_cache
def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    counter = Counter(A)

    res = 0
    if len(counter) < 3:
        print(res)
        return
    
    nums = len(counter)
    res = factorial(N+nums-1)//(factorial(N-3)*factorial(3))
    print(res)
    for _, v in counter.items():
        res //= factorial(v)

    print(res)

if __name__ == '__main__':
    main()