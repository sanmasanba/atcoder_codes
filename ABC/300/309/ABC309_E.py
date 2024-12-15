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
    N, M = map(int, input().split(' '))
    p = [0] + list(map(lambda x: int(x)-1, input().split(' ')))
    
    # dp[i] := 人iは何代先まで補償可能か
    # 複数の保険にはいっていても、最大期間のものだけ考えればよい
    dp = [-1]*N
    for i in range(M):
        x, y = map(int, input().split(' '))
        dp[x-1] = max(dp[x-1], y)

    for i in range(1, N):
        dp[i] = max(dp[i], dp[p[i]]-1)

    res = 0
    for i in range(N):
        if -1 < dp[i]:
            res += 1
    
    print(res)

if __name__ == '__main__':
    main()