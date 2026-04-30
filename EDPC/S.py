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
    K = list(map(int, list(input().strip())))
    D = int(input())
    # dp[i][j][k][l] := 上からi桁目まで確定していて、桁和をDで割ったあまりが
    #                   jとなるようなものの数(k:=K未満確定か否か)
    dp = [[[0]*2 for _ in range(101)] for _ in range(10001)]
    dp[0][0][0] = 1

    for i in range(len(K)):
        for j in range(D):
            # i+1桁目の値
            for x in range(10):
                # 1) K未満が確定してないところからの遷移
                # i+1桁目がkのi+1桁目のとき、
                if x == K[i]: dp[i+1][(j+x)%D][0] = (dp[i+1][(j+x)%D][0] 
                                                     + dp[i][j][0]) % MOD1e7
                if x < K[i]: dp[i+1][(j+x)%D][1] = (dp[i+1][(j+x)%D][1] 
                                                         + dp[i][j][0]) % MOD1e7
                # 2) K未満確定からの遷移
                dp[i+1][(j+x)%D][1] = (dp[i+1][(j+x)%D][1] 
                                       + dp[i][j][1]) % MOD1e7
                
    print((dp[len(K)][0][0] + dp[len(K)][0][1] - 1) % MOD1e7)

if __name__ == '__main__':
    main()