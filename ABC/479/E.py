# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
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
    A, B = map(list, zip(*[list(map(int, input().split())) for _ in range(N-1)]))
    A.append(0)
    B.append(1)

    # 0 を追加して、根付き木とする
    G = [[] for _ in range(N+1)]
    for i in range(N):
        a, b = A[i], B[i]
        G[a].append(b)
        G[b].append(a)
    
    c = [0] * (N+1)
    d = [0] * (N+1)
    seen = set()
    def dfs1(cur = 0, dp = 0):
        seen.add(cur)
        d[cur] = dp
        for nxt in G[cur]:
            if nxt in seen:
                continue
            c[cur] += dfs1(nxt, dp+1)
        seen.remove(cur)
        c[cur] += 1

        return c[cur]
    
    dfs1()

    res = [0] * (N+1)
    for i, (a, b) in enumerate(zip(A[:-1], B[:-1]), start=1):
        # どちらか一方がもう一方の部分木なので、小さいほうの補集合を計算
        ac, bc = c[a], c[b]
        if ac < bc:
            bc = N - ac
        elif bc < ac:
            ac = N - bc

        # print(f'a: {a}, ac: {ac}, b: {b}, bc: {bc}')
        if ac < bc:
            if d[a] < d[b]:
                res[b] += i
            elif d[b] < d[a]:
                res[1] += i
                res[a] -= i
        elif bc < ac:
            if d[b] < d[a]:
                res[a] += i
            elif d[a] < d[b]:
                res[1] += i
                res[b] -= i

    # DFS
    seen = set()
    def dfs2(cur = 0):
        seen.add(cur)

        for nxt in G[cur]:
            if nxt in seen:
                continue
            res[nxt] += res[cur]
            dfs2(nxt)
        seen.remove(cur)

    dfs2()
    print(*res[1:])

if __name__ == '__main__':
    main()
