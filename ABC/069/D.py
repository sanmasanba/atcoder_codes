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
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    
    res = [[INF]*(W+2)]
    for _ in range(H):
        res.append([INF] + [0]*W + [INF])
    res.append([INF]*(W+2))

    ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    vx, vy = 1, 1
    cnt = 0
    for i, a in enumerate(A, start=1):
        for _ in range(a):
            # paint
            res[vx][vy] = i

            # update
            nx, ny = vx+ds[cnt][0], vy+ds[cnt][1] 
            if res[nx][ny] != 0:
                cnt = (cnt+1)%4
                nx, ny = vx+ds[cnt][0], vy+ds[cnt][1] 
            vx, vy = nx, ny
    
    # output
    for r in res[1:-1]:
        print(*r[1:-1])

if __name__ == '__main__':
    main()