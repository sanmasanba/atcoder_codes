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
    N = int(input())

    n = len(str(bin(N))[2:])
    mask = []
    for i in range(n):
        if N >> i & 1:
            mask.append(n-1-i)

    res = []
    M = len(mask)
    for i in range(2**M):
        x = ['0']*n
        for m in range(M):
            if i >> m & 1:
                x[mask[m]] = '1'
        res.append(int(''.join(x), 2))
    
    print(*sorted(res), sep='\n')

if __name__ == '__main__':
    main()