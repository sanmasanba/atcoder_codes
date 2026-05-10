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
    N, S = map(int, input().split(' '))
    A, B = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    
    dp = [[False]*10001 for _ in range(N+1)]
    dp[0][0] = True

    for card in range(N):
        a, b = A[card], B[card]
        for i in range(10001):
            if dp[card][i] and i + a < 10001:
                dp[card+1][i+a] = True
            if dp[card][i] and i + b < 10001:
                dp[card+1][i+b] = True
    
    if dp[N][S]:
        print('Yes')
        
        res = deque()
        for i in range(N-1, -1, -1):
            a, b = A[i], B[i]
            if dp[i][S-a]:
                res.appendleft('H')
                S -= a
            elif dp[i][S-b]:
                res.appendleft('T')
                S -= b
        print(''.join(res))

    else:
        print('No')

if __name__ == '__main__':
    main()