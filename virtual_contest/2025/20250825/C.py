# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def g_input(N):
    M = int(input())
    G = [[False]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1][b-1] = True
        G[b-1][a-1] = True
    return M, G

# main
def main():
    # intput
    N = int(input())
    Mg, G = g_input(N)
    Mh, H = g_input(N)
    A = [list(map(int, input().split())) for _ in range(N-1)]

    res = INF
    for perm in permutations(range(N)):
        cost = 0
        for i in range(N):
            for j in range(i+1, N):
                if H[i][j] != G[perm[i]][perm[j]]:
                    cost += A[i][j-i-1]
        res = min(res, cost)
    print(res)

if __name__ == '__main__':
    main()