#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split(' '))
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    mapping = [-1] * N
    mapping[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nxtv in G[v]:
            if mapping[nxtv] != -1:
                continue
            mapping[nxtv] = (mapping[v]+1)%2
            que.append(nxtv)
    
    map0 = [i+1 for i, c in enumerate(mapping) if c == 0]
    map1 = [i+1 for i, c in enumerate(mapping) if c == 1]
    if N//2 <= len(map1):
        print(*map1[:N//2])
    else:
        print(*map0[:N//2])

if __name__ == '__main__':
    main()