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

#main
def main():
    # intput
    N, Q = map(int, input().split(' '))
    maxx, minx, maxy, miny = -INF, INF, -INF, INF
    P = []
    for _ in range(N):
        x, y = map(int, input().split(' '))
        X = x + y
        Y = x - y
        maxx = max(maxx, X)
        minx = min(minx, X)
        maxy = max(maxy, Y)
        miny = min(miny, Y)
        P.append((X, Y))
    
    res = []
    for _ in range(Q):
        query = int(input())-1
        Xi, Yi = P[query]
        res.append(max(Xi-minx, maxx-Xi, Yi-miny, maxy-Yi))

    # output    
    print(*res, sep='\n')
        
if __name__ == '__main__':
    main()