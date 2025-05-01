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
    N, D = map(int, input().split())
    A = list(map(int, input().split()))

    # D = 0なら要素は1つだけ残して他は消す
    if D == 0:
        cnt = Counter(A)
        res = 0
        for v in cnt.values():
            res += v-1
        print(res)
        return

    # それぞれをカウント
    L = [0] * (10**6+1)
    for a in A: 
        L[a] += 1

    def solver(s):
        tmp = L[s::D]
        if not tmp:
            return 0
        dp = [0] * (len(tmp)+1)
        for i in range(1, len(tmp)):
            # s+Diを0とする場合
            # -> s+D(i-1)はなんでもよいので、dp[i-1] + tmp[i]
            # s+Diを0としない場合
            # -> s+D(i-1)を操作する必要があるので,dp[i] + tmp[i-1]
            dp[i+1] = min(dp[i] + tmp[i], dp[i-1] + tmp[i-1])
        return dp[-1]

    # d = 0, .., D-1について考える
    res = 0
    for d in range(D):
        res += solver(d)
    print(res)

if __name__ == '__main__':
    main()