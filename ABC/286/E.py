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
    A = list(map(int, input().split()))
    S = [input().strip() for _ in range(N)]
    # 都市iから都市jをk本経由していくときの最小コスト
    dp = [(INF, -INF) for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 'Y':
                dp[i*N+j] = (1, -A[i]-A[j])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                (crr_dist, crr_cost) = dp[i*N+j]
                (ik_dist, ik_cost) = dp[i*N+k]
                (kj_dist, kj_cost) = dp[k*N+j]
                if ik_dist+kj_dist < crr_dist:
                    dp[i*N+j] = (ik_dist+kj_dist, ik_cost+kj_cost+A[k])
                elif (ik_dist+kj_dist == crr_dist 
                      and ik_cost+kj_cost+A[k] < crr_cost):
                    dp[i*N+j] = (ik_dist+kj_dist, ik_cost+kj_cost+A[k])
                   
    Q = int(input())    
    def solver():
        s, t = map(lambda x: int(x)-1, input().split())
        (miroot, micost) = dp[s*N+t]
        if miroot == INF:
            print('Impossible')
        else:
            print(miroot, -micost)

    for _ in range(Q):
        solver()        

if __name__ == '__main__':
    main()