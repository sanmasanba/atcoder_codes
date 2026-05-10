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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    log = defaultdict(int)
    for a in A:
        log[a] += a
    indiv_sum = sorted([v for v in log.values()])
    if len(indiv_sum) < K:
        print(0)
        return
    top_k = indiv_sum[:len(indiv_sum)-K]
    print(sum(top_k))

if __name__ == '__main__':
    main()