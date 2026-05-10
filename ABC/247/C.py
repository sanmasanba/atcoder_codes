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
def  solve(N):
    if N == 1:
        return [1]
    else:
        return [*solve(N-1), N, *solve(N-1)]

#main
def main():
    N = int(input())    
    print(*solve(N))

if __name__ == '__main__':
    main()