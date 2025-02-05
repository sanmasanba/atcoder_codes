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
    N, X = map(int, input().split())
    dp = [[-INF]*(X+1) for _ in range(3)]
    for i in range(3): dp[i][0] = 0
    
    # i番目の食品によって、摂取カロリーがjあるいはj-cになった時の
    # ビタミンviの最大接種量
    for i in range(N):
        v, a, c = map(int, input().split())
        for j in range(X, c-1, -1):
            dp[v-1][j] = max(dp[v-1][j], dp[v-1][j-c]+a)
    # j[cal]まで摂取したときのビタミンiの最大接種量
    for i in range(3):
        for j in range(X):
            dp[i][j+1] = max(dp[i][j], dp[i][j+1])
    
    # 貪欲に一番摂取カロリーが小さいものを食べていく
    idx = [0, 0, 0]
    for i in range(X):
        if dp[0][idx[0]]<=dp[1][idx[1]] and dp[0][idx[0]]<=dp[2][idx[2]]:
            idx[0] += 1
        elif dp[1][idx[1]]<=dp[0][idx[0]] and dp[1][idx[1]]<=dp[2][idx[2]]:
            idx[1] += 1
        else:
            idx[2] += 1
    print(min(dp[0][idx[0]], dp[1][idx[1]], dp[2][idx[2]]))

if __name__ == '__main__':
    main()