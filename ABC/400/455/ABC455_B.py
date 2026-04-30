# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    H, W = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]

    res = 0
    for h in range(1, H+1):
        for w in range(1, W+1):
            for r in range(H):
                for c in range(W):
                    if not (0 <= r+h <= H and 0 <= c+w <= W):
                        continue
                    tmp = S[r:r+h]
                    if [row[c:c+w] for row in tmp] == [row[c:c+w][::-1] for row in tmp][::-1]:
                        res += 1
    print(res)

if __name__ == '__main__':
    main()