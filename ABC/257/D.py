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
    N = int(input())
    xs, ys, Ps = [], [], []
    for _ in range(N):
        x, y, p = map(int, input().split())
        xs.append(x)
        ys.append(y)
        Ps.append(p)
    
    res = INF
    for s in range(N):
        lo = 0
        hi = 10**10
        while lo+1 < hi:
            mi = (hi+lo)//2
            reached = [0]*N
            reached[s] = 1
            dp = [s]
            while dp:
                i = dp.pop()
                for j in range(N):
                    if reached[j]:
                        continue
                    if (abs(xs[i]-xs[j])+abs(ys[i]-ys[j])) <= Ps[i]*mi:
                        reached[j] = 1
                        dp.append(j)
            if all(reached):
                hi = mi
            else:
                lo = mi
        res = min(res, hi)
    print(res)

if __name__ == '__main__':
    main()