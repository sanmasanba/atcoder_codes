# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
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
    N = int(input())
    A = [[0]*(2*N) for _ in range(2*N)]
    for i in range(2*N-1):
        for j, a in enumerate(map(int, input().split()), start=i+1):
            A[i][j] = a
            A[j][i] = a
    
    use = [False]*(2*N)
    def dfs(res=0, pre=0):
        if all(use):
            return max(res, pre)
        for a in range(2*N):
            if use[a]:
                continue
            use[a] = True
            for b in range(a, 2*N):
                if use[b]:
                    continue
                use[b] = True
                res = dfs(res, pre ^ A[a][b])
                use[b] = False
            use[a] = False
            return res

    print(dfs())

if __name__ == '__main__':
    main()