#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

def dfs1(G: List[List[int]], v: int, used: List[bool], I: List[int]):
    used[v] = True
    for nextv in G[v]:
        if not used[nextv]:
            dfs1(G, nextv, used, I)
    I.append(v)

def dfs2(G: List[List[int]], v: int, used: List[bool]):
    global cnts
    used[v] = True
    cnts += 1
    for nextv in G[v]:
        if not used[nextv]:
            dfs2(G, nextv, used)

#main
def main():
    # intput
    N, M = map(int, input().split(' '))
    A = [0] * (M+1)
    B = [0] * (M+1)
    G = [[] for _ in range(N+1)]
    H = [[] for _ in range(N+1)]
    used = [False] * (N+1)
    I = []
    for i in range(M):
        A[i], B[i] = map(int, input().split(' '))
        G[A[i]].append(B[i])
        H[B[i]].append(A[i])
    
    # scc
    for i in range(1, N+1):
        if not used[i]:
            dfs1(G, i, used, I)
    
    res = 0
    I.reverse()
    used = [False] * (N+1)
    global cnts
    for i in I:
        if used[i]:
            continue
        cnts = 0
        dfs2(H, i, used)
        res += (cnts * (cnts-1)) // 2
    
    print(res)

if __name__ == '__main__':
    main()