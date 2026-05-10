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
    dots = [tuple(map(int, input().split())) for _ in range(N)]
    dots_split = defaultdict(set)

    for x, y in dots:
        dots_split[x].add(y)

    dots_x_split = []
    for x, v in dots_split.items():
        if 1 < len(v):
            dots_x_split.append(v)
    
    if len(dots_x_split) < 2:
        print(0)
        return
    
    res = 0
    for pp1, pp2 in combinations(dots_x_split, 2):
        for p1, p2 in combinations(pp1, 2):
            if p1 in pp2 and p2 in pp2:
                res += 1

    print(res)

if __name__ == '__main__':
    main()