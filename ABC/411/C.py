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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    grid = [0]*(N+2)
    res = 0
    for a in A:
        left, right = 1, 1
        left = grid[a-1]
        right = grid[a+1]
        grid[a] ^= 1
        
        if left != right:
            pass
        elif left and right: 
            if grid[a]: res -= 1
            elif not grid[a]: res += 1
        elif not left and not right:
            if grid[a]: res += 1
            elif not grid[a]: res -= 1
        print(res)


if __name__ == '__main__':
    main()