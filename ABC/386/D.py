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
    N, M = map(int, input().split())
    XYC = []
    for _ in range(M):
        x, y, c = input().split()
        XYC.append((int(x), int(y), c))
    XYC.sort()
    y_lim = INF
    res = True
    for x, y, c in XYC:
        if c == 'W':
            y_lim = min(y_lim, y)
        if c == 'B':
            if y >= y_lim:
                res = False
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()