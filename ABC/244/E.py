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
MOD = 998244353

#main
def main():
    # intput
    N, M, K, S, T, X = map(int, input().split(' '))
    S -= 1
    T -= 1
    X -= 1
    edge = []
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        edge.append((a, b))
    
    # dp[i][j][k] := 頂点Sから辺をi回通って頂点jへ行き、途中で頂点Xを
    #                (通った回数) mod 2 = xであるような方法の数
    dp = [[[0]*N for _ in range(K+1)] for _ in range(2)]
    dp[0][0][S] = 1
    
    for i in range(K):
        for U, V in edge:
            for x in range(2):
                # 次に行くノードがXなら偶奇を入れ替える
                dp[x][i+1][V] += dp[x^(V==X)][i][U]
                if dp[x][i+1][V] >= MOD:
                    dp[x][i+1][V] -= MOD
                dp[x][i+1][U] += dp[x^(U==X)][i][V]
                if dp[x][i+1][U] >= MOD:
                    dp[x][i+1][U] -= MOD

    print(dp[0][K][T])

if __name__ == '__main__':
    main()