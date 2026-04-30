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
    S = input().strip()
    T = input().strip()

    dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]
    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if 0 < i and 0 < j and S[i-1] == T[j-1]:
                dp[i][j] = max(dp[i-1][j], 
                               dp[i][j-1], 
                               dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i-1][j] if 0 < i else 0, 
                               dp[i][j-1] if 0 < j else 0)

    print(max(dp[-1]))

if __name__ == '__main__':
    main()