#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    N, M = map(int, input().split())
    A = [int(''.join(input().split()), base=2) for _ in range(M)]

    dp = [[1000]*(2**N) for _ in range(M+1)]
    dp[0][0] = 0

    for i in range(M):
        for state in range(2**N):
            if dp[i][state] == INF: continue
            dp[i+1][state|A[i]] = min(dp[i+1][state|A[i]], 
                                      dp[i][state]+1)
            dp[i+1][state] = min(dp[i+1][state], dp[i][state])

    print(-1 if dp[-1][-1] == 1000 else dp[-1][-1])

if __name__ == '__main__':
    main()