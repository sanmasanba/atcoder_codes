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
    N, D = map(int, input().split(' '))
    walls = []
    for _ in range(N):
        L, R = map(int, input().split(' '))
        walls.append((L, R))
    walls.sort(key=lambda x:x[1])

    res = 0
    x = -INF
    for l , r in walls:
        if x + D - 1 < l:
            res += 1
            x = r 

    print(res)

if __name__ == '__main__':
    main()