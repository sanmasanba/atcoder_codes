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

# main
def main():
    # intput
    N, M = map(int, input().split())
    G = [[-INF]*N for _ in range(N)]
    for _ in range(M):
        s, g, weight = map(int, input().split())
        G[s-1][g-1] = max(G[s-1][g-1], weight)
        G[g-1][s-1] = max(G[g-1][s-1], weight)
    
    res = -1
    for perm in permutations(range(N)):
        tmp = 0
        for i in range(N-1):
            s, g = perm[i], perm[i+1]
            tmp += G[s][g]
            res = max(tmp, res)
    print(res)

if __name__ == '__main__':
    main()