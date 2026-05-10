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
    sx, sy, tx, ty = map(lambda x: int(x)+1000, input().split())
    
    res = ''
    for _ in range(sx, tx): res += 'R'
    for _ in range(sy, ty): res += 'U'
    for _ in range(sx, tx): res += 'L'
    for _ in range(sy, ty): res += 'D'

    res += 'D'
    for _ in range(sx, tx+1): res += 'R'
    for _ in range(sy, ty+1): res += 'U'
    res += 'L'
    res += 'U'
    for _ in range(sx, tx+1): res += 'L'
    for _ in range(sy, ty+1): res += 'D'
    res += 'R'

    print(res)

if __name__ == '__main__':
    main()