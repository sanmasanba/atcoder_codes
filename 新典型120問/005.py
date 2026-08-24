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

def move(n):
    tmp = list(str(n))
    return int(''.join([tmp[-1]] + tmp[:-1]))

def bfs(a, n):
    stc = [(0, 1)]
    used = [INF]*(10**7)
    used[1] = 0
    while stc:
        st, x = heappop(stc)
        if used[x] < st:
            continue
        y = a * x
        res = st + 1
        if y < 10**7 and res < used[y]:
            used[y] = res
            heappush(stc, (res, y))
        y = move(x)
        if x%10 > 0 and x >= 10 and res < used[y]:
            used[y] = res
            heappush(stc, (res, y))
    return used[n] if used[n] < INF else -1

# main
def main():
    # intput
    a, N = map(int, input().split())
    print(bfs(a, N))

if __name__ == '__main__':
    main()