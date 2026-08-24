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
    N, S = map(int, input().split())
    A, B = zip(*[list(map(int, input().split())) for _ in range(N)])

    dp = [[[False]*(S+1) for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0] = True

    for i in range(N):
        for k in range(S+1):
            for j in range(2):
                # dp[i][j][k] := i枚目をjにしたときkがありえるなら１
                if k-A[i] >= 0:
                    dp[i+1][0][k] |= dp[i][j][k-A[i]]
                if k-B[i] >= 0:
                    dp[i+1][1][k] |= dp[i][j][k-B[i]]

    res = []
    idx = S
    for i in range(N, 0, -1):
        # どちらかの面があればいいので、逆にたどるだけでいい
        if dp[i][0][idx]:
            res.append('H')
            idx -= A[i-1]
        elif dp[i][1][idx]:
            res.append('T')
            idx -= B[i-1]
        else:
            break
    if len(res) != N:
        print('No')
    else:
        print('Yes')
        print(''.join(res[::-1]))

if __name__ == '__main__':
    main()
