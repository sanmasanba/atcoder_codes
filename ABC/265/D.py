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
    N, P, Q, R = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    y, z, w = 0, 0, 0
    s0, s1, s2 = 0, 0, 0
    res = False
    for x in range(N):
        # xを固定してそれぞれ区間ごとに満たすかを調べる
        while y < N and s0 < P:
            s0 += A[y]
            s1 -= A[y]
            y += 1
        while z < N and s1 < Q:
            s1 += A[z]
            s2 -= A[z]
            z += 1
        while w < N and s2 < R:
            s2 += A[w]
            s2 += A[w]
            w += 1
        if s0 == P and s1 == Q and s2 == R:
            res = True
            break
        s0 -= A[x]        

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()