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
    X, Y, Z = [], [], []
    for _ in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    
    dist = [[INF]*N for _ in range(N)]
    for i, j in combinations(range(N), 2):
        d = abs(X[i]-X[j]) + abs(Y[i]-Y[j])
        dist[i][j] = d + max(0, Z[j]-Z[i])
        dist[j][i] = d + max(0, Z[i]-Z[j])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # dp[i][j] := iで表される都市に行ったことがあるとき、現在jにいるときの最小距離
    dp = [[INF]*N for _ in range(1<<N)]
    dp[0][0] = 0
    for state in range(1, 1<<N):
        for i in range(N):
            if state >> i & 1:
                pre_state = state - (1 << i)
                for j in range(N):
                    if i == j or (pre_state << j) & 1:
                        continue
                    dp[state][i] = min(dp[state][i], 
                                       dp[pre_state][j] + dist[j][i])

    print(dp[(1<<N)-1][0])

if __name__ == '__main__':
    main()