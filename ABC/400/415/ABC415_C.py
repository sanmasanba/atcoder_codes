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
    S = ['0']
    S.extend(input().strip())
    dp = [False]*(1<<N)
    dp[0] = True

    for mask in range(2**N):
        for i in range(N):
            # 混ぜたときに薬にiが含まれない
            # iを混ぜても危険じゃない
            if ((mask >> i)&1)==0 and S[mask|(1<<i)] == '0' and dp[mask]:
                dp[mask|(1<<i)] = True
        if dp[-1]:
            print('Yes')
            return
    print('No')

#main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solver()

if __name__ == '__main__':
    main()