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
    X, Y = map(int, input().split(' '))
    A, B = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    
    # 
    dp = [[[INF] * 301 for _ in range(301)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for a in range(301):
            for b in range(301):
                dp[i+1][a][b] = min(dp[i][a][b], dp[i+1][a][b])
                na, nb = min(300, a+A[i]), min(300, b+B[i])
                dp[i+1][na][nb] = min(dp[i][a][b]+1, dp[i+1][na][nb])

    res = INF
    for x in range(X, 301):
        for y in range(Y, 301):
            res = min(res, dp[N][x][y])

    print(-1 if res == INF else res)


if __name__ == '__main__':
    main()