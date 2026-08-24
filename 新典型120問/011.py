# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    S = [list(input().strip()) for _ in range(N)]
    Q = int(input())

    # 1-1) それぞれの都市に関して、i->j への変数inf, 価値-inf で初期化
    dp = [[(INF, -INF)]*N for _ in range(N)]
    # 1-2) 到達可能な辺を初期化
    for i in range(N):
        for j in range(N):
            if S[i][j] == 'Y':
                dp[i][j] = (1, A[i] + A[j])
    
    # 2-1) i->k->j と i->j を比較しながら更新
    for k in range(N):
        for i in range(N):
            for j in range(N):
                cur_dist, cur_val = dp[i][j]
                nxt_dist = dp[i][k][0] + dp[k][j][0]
                nxt_val = dp[i][k][1] + dp[k][j][1] - A[k]
                if cur_dist < nxt_dist:
                    dp[i][j] = (cur_dist, cur_val)
                elif nxt_dist < cur_dist:
                    dp[i][j] = (nxt_dist, nxt_val)
                else:
                    dp[i][j] = (cur_dist, max(cur_val, nxt_val))

    for _ in range(Q):
        U, V = map(lambda x: int(x)-1, input().split())
        dist, val = dp[U][V]
        if dist == INF:
            print('Impossible')
        else:
            print(dist, val)

if __name__ == '__main__':
    main()
