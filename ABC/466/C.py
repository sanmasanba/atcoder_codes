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
    N = int(input())

    res = 0
    r = 1
    for l in range(1, N):
        r = max(l+1, r)
        print('?', l, r, flush=True)
        in_ = input().strip()
        if in_ == 'Yes':
            while r < N:
                r += 1
                print('?', l, r, flush=True)
                in_ = input().strip()
                if in_ == 'No':
                    break
        res += r-l-(1 if in_ == 'No' else 0)

    print('!', res, flush=True)
        
if __name__ == '__main__':
    main()