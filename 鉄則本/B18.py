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
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [[False]*(10001) for _ in range(61)]
    dp[0][0] = True
    for i in range(N):
        a = A[i]
        for s in range(10001):
            if dp[i][s]:
                dp[i+1][s] = True
                if s+a <= 10000:
                    dp[i+1][s+a] = True
    if not dp[N][S]:
        print(-1)
        return

    res = []
    s = S
    for i in range(N, 0, -1):
        if 0 <= s-A[i-1] and dp[i-1][s-A[i-1]]:
            res.append(i)
            s -= A[i-1]
        if s == 0:
            break

    print(len(res))
    print(*res[::-1])

if __name__ == '__main__':
    main()