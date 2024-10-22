#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    x = [0] * 1001
    y = [0] * 1001
    lxs, lys, rxs, rys = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    MAP = [[0 for _ in range(1001)] for _ in range(1001)]
    for lx, ly, rx, ry in zip(lxs, lys, rxs, rys):
        MAP[ly][lx] += 1
        MAP[ry][rx] += 1
        MAP[ly][rx] -= 1
        MAP[ry][lx] -= 1

    # ２次元いもす法を使う
    res = [0] * (N+1)
    for i in range(1001):
        MAP[i] = list(accumulate(MAP[i]))
    res_MAP = []
    for arr in zip(*MAP):
        res_MAP.append(list(accumulate(arr)))
    for i in range(1001):
        for j in range(1001):
            res[res_MAP[j][i]] += 1

    print(*res[1:], sep='\n')

if __name__ == '__main__':
    main()