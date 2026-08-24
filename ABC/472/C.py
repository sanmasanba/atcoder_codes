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
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    memo = deque()
    kal = 0
    res = []
    for i, a in enumerate(A, start=1):
        kal += a
        if kal <= K:
            res.append('Yes')
            memo.append((a, i))
        else:
            res.append('No')
            kal -= a

        while memo:
            b, j = memo[0]
            if j <= i - M + 1:
                b, j = memo.popleft()
                kal -= b
            else:
                break
    print(*res, sep='\n')

if __name__ == '__main__':
    main()
