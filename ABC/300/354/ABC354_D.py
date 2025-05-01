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
    A, B, C, D = map(int, input().split())
    
    BASE = 40_000_000_000
    res = 0
    grid = [[2, 1, 0, 1],
            [1, 2, 1, 0]]
    
    for y in range(2):
        for x in range(4):
            x1 = (A - x + 3 + BASE)//4
            x2 = (C - x + 3 + BASE)//4
            y1 = (B - y + 1 + BASE)//2
            y2 = (D - y + 1 + BASE)//2
            res += (x2 - x1) * (y2 - y1) * grid[y][x]
    
    print(res)    

if __name__ == '__main__':
    main()