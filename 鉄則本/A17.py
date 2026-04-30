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
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    dist = [INF]*N
    dist[0] = 0
    for i in range(1, N):
        dist[i] = min(dist[i], dist[i-1]+A[i-1])
        if 1 < i: dist[i] = min(dist[i], dist[i-2]+B[i-2])

    pos = N
    res = [pos]
    while 1 < pos:
        d = dist[pos-1]

        if d-A[pos-2] == dist[pos-2]:
            res.append(pos-1)
            pos -= 1
        else:
            res.append(pos-2)
            pos -= 2

    print(len(res))
    print(*res[::-1])

if __name__ == '__main__':
    main()