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
    C = [0] + list(map(int, input().split()))
    A = [1] + list(map(int, input().split()))
    # L[i] := iから移動可能な茶碗
    L = [i - C[i] for i in range(N)]

    res = 0
    for i in range(N-1, 0, -1):
        # 豆がないならスルー
        if A[i] == 0: continue

        # 豆があるとき、以下のルールで移動
        res += 1
        l = L[i]
        # 茶碗[l:i]に豆があるとき、そのうち最も後ろの茶碗に移動
        if any(A[j] for j in range(i-1, l-1, -1)):
            continue
        # ないとき、最もLが小さい茶碗[l:i]に移動
        mn = 1 << 60
        argmn = -1
        for j in range(i-1, l-1, -1):
            if mn > L[j]:
                mn = L[j]
                argmn = j
        A[argmn] = 1
    
    print(res)

if __name__ == '__main__':
    main()