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

def solve(N, r, x):
    l = 1
    while l+1 < r:
        mid = (l+r)//2
        tmp = N//mid

        if x < tmp:
            l = mid
        else:
            r = mid
    return l

#main
def main():
    # intput
    N = int(input())
    
    res = 0
    x = 1
    r = N
    while x != N:
        l = solve(N, r, x)
        res += x * (r - l)
        r = l
        x = N//l

    print(res + N)

if __name__ == '__main__':
    main()