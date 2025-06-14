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
    N = int(input())
    S = list(input().strip())
    # 区間[l, r)を全て1の区間にすることを考える
    # 0と1の累積個数列cnt0とcnt1とすれば、操作回数は
    # 1 ... l-1 : cnt1[l-1]
    # l-1 ... r-1 : cnt0[r-1] -cnt0[l-1]
    # r ... N : cnt1[N] - cnt1[r-1]
    # ∴res = cnt1[l-1] + cnt0[r-1] - cnt0[l-1] + cnt1[N] - cnt1[r-1] + cnt1[l-1]
    # ここで、C = cnt0 - cnt1 とすれば、
    # res = cnt1[N] + C[r-1] - C[l-1]なのでC[i]について最小の値を求めればよい
    C = [0]*(N+1)
    cnt1 = 0
    for i in range(N): 
        if S[i] == '0':
            C[i+1] = C[i] + 1
        else:
            cnt1 += 1
            C[i+1] = C[i] - 1
    
    cmax, res = 0, 0
    for r in range(N+1):
        # cmaxは、C[r]を固定したときの[0, r)の区間で最大となるC[l]に相当する
        res = min(res, C[r]-cmax)
        cmax = max(cmax, C[r])
    print(cnt1 + res)

#main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solver()
    
if __name__ == '__main__':
    main()