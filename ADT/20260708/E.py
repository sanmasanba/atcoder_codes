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
    Q = int(input())
    stc = [0]

    cur = 0
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            stc.append(stc[-1] + q[1])
        elif q[0] == 2:
            cur += 1
        else:
            print(stc[cur+q[1]-1]-stc[cur])

if __name__ == '__main__':
    main()