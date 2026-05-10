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

def f(a, b):
    return [min(a, b), max(a, b)]

#main
def main():
    # intput
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
    
    if N != M:
        print('No')
        return
    
    #BFS
    def bfs(N, s=0):
        dist = [False for _ in range(N)]
        queue = deque()
        dist[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            for next_v in G[v]:
                if dist[next_v]:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        return all(dist)
    
    # 「連結成分が一つ」かつ「全ての頂点から辺が2本ずつ出ている」
    print('Yes' if (bfs(N) and all([len(x)==2 for x in G])) else 'No')

if __name__ == '__main__':
    main()