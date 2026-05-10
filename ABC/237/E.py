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
INF = 1 << 60

#main
def main():
    # intput
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = defaultdict(list)
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        G[u].append((v, max(0, H[v]-H[u])))
        G[v].append((u, max(0, H[u]-H[v])))

    que = []
    heappush(que, 0)
    score = [INF]*N
    score[0] = 0
    bit = 18
    bit_mask = (1<<bit)-1
    while que:
        tmp = heappop(que)
        curr_score, curr = tmp>>bit, tmp&bit_mask
        
        if score[curr] < curr_score:
            continue
        for nxt, d in G[curr]:
            if score[nxt] > score[curr]+d:
               score[nxt] = score[curr]+d
               heappush(que, (score[nxt]<<bit)+nxt)
    print(-min(score[i]-H[0]+H[i] for i in range(N)))

if __name__ == '__main__':
    main()