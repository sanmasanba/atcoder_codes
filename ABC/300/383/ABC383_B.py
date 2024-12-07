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

def manhattan_distance(x1: T, x2: T, y1: T, y2: T) -> T:
    return abs(x2-x1) + abs(y2-y1)

#main
def main():
    # intput
    H, W, D = map(int, input().split(' '))
    S = [list(input()) for _ in range(H)]

    sample = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                sample.append((h, w))

    def solve(p, D):
        res = set()
        for s in sample:
            if manhattan_distance(p[0], s[0], p[1], s[1]) <= D:
                res.add(s)
        return res

    res = 0
    for combi in combinations(sample, 2):
        a, b = combi
        tmp = set()
        tmp |= solve(a, D)
        tmp |= solve(b, D)
        res = max(res, len(tmp))

    print(res)

if __name__ == '__main__':
    main()