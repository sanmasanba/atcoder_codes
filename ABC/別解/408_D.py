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

def solver():
    # intput
    N = int(input())
    S = list(input().strip())
    
    # dp[i][j] := j-1までが確定していて、iをjにするときにかかるコスト
    # j = 1 -> jを0にする
    # j = 2 -> jを1にする
    # j = 3 -> jを0にする
    dp = [[0]*(3) for _ in range(N+1)]
    for i in range(N):
        # ...00 + 0
        dp[i+1][0] = dp[i][0] + (1 if S[i]=='1' else 0)
        # ...00 + 1 or ...0...1 + 1
        dp[i+1][1] = min(dp[i][0], dp[i][1]) + (1 if S[i]=='0' else 0)
        # ...00 + 2 or ...0...1 + 2 or ...0...1...2 + 2
        dp[i+1][2] = (min(dp[i][0], dp[i][1], dp[i][2]) 
                        + (1 if S[i]=='1' else 0))
    print(min(dp[-1]))

#main
def main():
    # input
    T = int(input())
    for _ in range(T):
        solver()

if __name__ == '__main__':
    main()