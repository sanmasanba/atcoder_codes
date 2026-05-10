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

def check(x, N):
    res = True
    for i in range(N-1):
        if x[i] >= x[i+1]:
            res = False
    return res

#main
def main():
    N, M = map(int, input().split(' '))
    res = []
    for per in permutations([i+1 for i in range(M)], N):
        if check(per, N):
            print(*per)

if __name__ == '__main__':
    main()  