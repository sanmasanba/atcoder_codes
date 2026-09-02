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
    N, M, S, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        # 有向グラフは次の列を削除
        G[b].append(a)
    

    # BFS
    def bfs(G, N, s):
        # dist:vからの距離, queue:探索キュー
        dist = [-1 for _ in range(N)]
        queue = deque()
        dist[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        return dist

    res = 0
    for d in bfs(G, N, S-1):
        if d < 0:
            continue
        elif d <= K:
            res += 1
    print(res)

if __name__ == '__main__':
    main()
