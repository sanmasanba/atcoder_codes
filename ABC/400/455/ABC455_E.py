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
    S = list(input().strip())
    
    cnt = defaultdict(int)
    cnt[(0, 0, 0)] = 1
    G = {(0, 0, 0):[]}

    def dfs(root, n):
        nxt = list(root)
        nxt[n] += 1
        nxt = tuple(nxt)
        cnt[nxt] += 1
        if nxt not in G[root]:
            G[root].append(nxt)
            G[nxt] = []
        else:
            dfs(nxt, n)

    for s in S:
        match s:
            case 'A': n = 0
            case 'B': n = 1
            case 'C': n = 2        
        dfs((0, 0, 0), n)
    
    print(cnt)

if __name__ == '__main__':
    main()