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
    x_maxx, x_minx = -INF, INF
    y_maxy, y_miny = -INF, INF
    for i in range(N):
        x, y = map(int, input().split())
        # xx = x+y, yy = x-y
        xx, yy = x+y, x-y
        x_minx = min(xx, x_minx)
        x_maxx = max(xx, x_maxx)
        y_miny = min(yy, y_miny)
        y_maxy = max(yy, y_maxy)

    print(max(abs(x_maxx-x_minx), abs(y_maxy-y_miny)))

if __name__ == '__main__':
    main()