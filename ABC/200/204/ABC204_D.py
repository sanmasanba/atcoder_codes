#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N = int(input())
    T = list(map(int, input().split(' ')))
    
    sum_time = sum(T)
    dp = [[False] * (sum_time + 1) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for t in range(sum_time+1):
            if t < T[i]:
                dp[i+1][t] = dp[i][t]
            else:
                dp[i+1][t] = dp[i][t - T[i]] | dp[i][t]
    
    res = INF
    for i, c in enumerate(dp[-1]):
        if c:
            time_a = i
            time_b = sum_time - i
            res = min(res, max(time_a, time_b))
    print(res)

if __name__ == '__main__':
    main()