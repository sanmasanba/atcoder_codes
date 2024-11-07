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
    As = []
    for _ in range(N):
        As.append(list(map(int, input().split((' ')))))
    M = int(input())
    XY = set()
    for _ in range(M): 
        XY.add(tuple(map(lambda x: int(x)-1, input().split(' '))))

    res = INF
    for perm in permutations(range(N)):
        run_time = 0
        for i, p in enumerate(perm):
            run_time += As[p][i]
        can_goal = True
        for i in range(N-1):
            pair1 = (perm[i], perm[i+1])
            pair2 = (perm[i+1], perm[i])
            if pair1 in XY or pair2 in XY:
                can_goal = False
        if can_goal:
            res = min(res, run_time)
    
    # output
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()