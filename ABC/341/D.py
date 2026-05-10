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

#main
def main():
    N, M, K = map(int, input().split(' '))
    
    L = (N*M)//gcd(N, M)
    l = 0
    r = int(2e18)
    while l+1 < r:
        mid = (l+r)//2
        y = (mid//N) + (mid//M) - 2*(mid//L)
        if y < K:
            l = mid
        else:
            r = mid

    print(r)

if __name__ == '__main__':
    main()