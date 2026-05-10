#library
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

#main
def main():
    # intput
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    bipartite = [0] * N
    component = []
    def dfs(v, c):
        bipartite[v] = c    
        cnt = [0, 0]
        cnt[c == -1] += 1
        stack = [(v, c)]
        edge = 0
        while stack:
            v, c = stack.pop()
            for nv in G[v]:
                edge += 1
                if bipartite[nv] == c:
                    return None
                if bipartite[nv] == 0:
                    bipartite[nv] = -c
                    cnt[-c == -1] += 1
                    stack.append((nv, -c))
        return (*cnt, edge//2)
    
    for i in range(N):
        if bipartite[i] == 0: 
            res = dfs(i, 1)
            if res is None:
                print(0)
                return
            component.append(res)

    # 存在しうる全エッジ
    res = N*(N-1)//2
    # 部分グラフの完全2部グラフを構築
    inner = sum((w+b)*(w+b-1)//2 for w, b, _ in component)
    # すべての達成可能な組み合わせ - 部分グラフ内の組み合わせ
    res -= inner
    for w, b, e in component:
        res += w*b - e
    print(res)

if __name__ == '__main__':
    main()