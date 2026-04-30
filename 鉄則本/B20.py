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
    S = list(input().strip())
    T = list(input().strip())
    
    dp = [[0]*(2001) for _ in range(2001)]
    for i in range(2001): 
        dp[0][i] = i
        dp[i][0] = i

    for i, s in enumerate(S, start=1):
        for j, t in enumerate(T, start=1):
            dp[i][j] = min(dp[i][j-1]+1, 
                           dp[i-1][j]+1, 
                           dp[i-1][j-1]+(0 if s == t else 1))
    print(dp[len(S)][len(T)])    

if __name__ == '__main__':
    main()