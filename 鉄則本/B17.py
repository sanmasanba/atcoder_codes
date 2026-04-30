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
    N = int(input())
    H = list(map(int, input().split()))
    
    dp = [INF]*(N+1)
    dp[1] = 0
    for i in range(1, N):
        if i+1 <= N: dp[i+1] = min(dp[i+1], dp[i]+abs(H[i]-H[i-1]))
        if i+2 <= N: dp[i+2] = min(dp[i+2], dp[i]+abs(H[i+1]-H[i-1]))
    
    pos = N
    res = [pos]
    while 1 < pos:
        if dp[pos] - abs(H[pos-1]-H[pos-2]) == dp[pos-1]: 
            pos -= 1
            res.append(pos)
        elif dp[pos] - abs(H[pos-1]-H[pos-3]) == dp[pos-2]: 
            pos -= 2
            res.append(pos)
    print(len(res))
    print(*res[::-1])

if __name__ == '__main__':
    main()