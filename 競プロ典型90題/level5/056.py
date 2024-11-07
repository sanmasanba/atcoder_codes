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
    
    # dp
    dp = [[False] * (S+1) for _ in range(N+1)]
    dp[0][0] = True
    for n in range(N):
        a, b = A[n], B[n]
        for s in range(1, S+1):
            if 0 <= s - a and dp[n][s-a] is True:
                dp[n+1][s] = True
            if 0 <= s - b and dp[n][s-b] is True:
                dp[n+1][s] = True
    
    if dp[N][S] == False:
        print('Impossible')  
        return

    # 経路復元
    tmp = ''
    s = S
    for n in range(N-1, -1, -1):
        a, b = A[n], B[n]
        if 0 <= s - a and dp[n][s-a] is True:
            tmp += 'A'
            s -= a
        elif 0 <= s - b and dp[n][s-b] is True:
            tmp += 'B'
            s -= b
    res = ''
    for s in tmp[::-1]: res += s
    print(res)

if __name__ == '__main__':
    main()