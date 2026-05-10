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
    # input
    N = int(input())
    A = list(map(int, input().split(' ')))
    num2pos = defaultdict(list)
    for i, a in enumerate(A):
        num2pos[a].append(i)
    
    res = []
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split(' '))
        if X not in num2pos:
            res.append(0)
            continue
        l_pos = bisect_left(num2pos[X], L-1)
        r_pos = bisect_right(num2pos[X], R-1)
        res.append(r_pos - l_pos)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()