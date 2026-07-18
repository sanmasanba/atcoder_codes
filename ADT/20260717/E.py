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
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(input().strip())
        dp = [False]*(2**N)
        dp[0] = True
        for bit in range(1, 2**N):
            for i in range(N):
                if (bit >> i) & 1:
                    dp[bit] |= dp[bit-(1<<i)] and S[bit-1]=='0'
        print('Yes' if dp[2**N-1] else 'No')

if __name__ == '__main__':
    main()