#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, K, P = map(int, input().split())
    C, A = [], []
    for _ in range(N):
        c, *a = list(map(int, input().split()))
        C.append(c)
        A.append(a)

    # dp[i][j] := 計画iまでを実行したときに、パラメータjを達成できる最小費用
    # j := (P+1)進数でパラメータを示したもの
    dp = [[INF] * (P + 1) ** K for _ in range(N + 1)]
    dp[0][0] = 0

    def decimal_to_base_P(n: int, base: int, K: int) -> str: 
        if n == 0: 
            return '0'.zfill(K) 
        res = [] 
        while n:
            res.append(int(n % base)) 
            n //= base 
        return ''.join(str(x) for x in res[::-1]).zfill(K)

    for i in range(N):
        cost = C[i]
        for p in range((P + 1) ** K):
            # 計画iを実行しない
            dp[i + 1][p] = min(dp[i + 1][p], dp[i][p])
            
            # 計画iを実行
            np = decimal_to_base_P(p, P+1, K)
            tmp = sum(min(P, int(np[K-k-1])+A[i][k])*((P+1)**k) for k in range(K))
            dp[i+1][tmp] = min(dp[i+1][tmp], dp[i][p] + cost)

    result = dp[N][(P + 1) ** K - 1]
    print(result if result != INF else -1)

if __name__ == '__main__':
    main()
