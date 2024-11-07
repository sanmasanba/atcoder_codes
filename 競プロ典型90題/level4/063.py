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
    H, W = map(int, input().split(' '))
    P = [list(map(int, input().split(' '))) for _ in range(H)]

    res = 0
    for bit in range(2**H):
        parm_matrix = []
        d = defaultdict(int)
        for mask in range(H):
            if bit >> mask & 1:
                parm_matrix.append(P[mask])
        rows = len(parm_matrix)
        for row in zip(*parm_matrix):
            if all(map(lambda x: row[0] == x, row)):
                d[row[0]] += rows
        for _, value in d.items():
            res = max(res, value)

    print(res)

if __name__ == '__main__':
    main()