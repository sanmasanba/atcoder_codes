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
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    AK = [[0]*M for _ in range(N)]
    for i in range(M):
        _, *a = list(map(int, input().split()))
        for aa in a: AK[aa-1][i] = 1
    
    res = INF
    for i in range(1, 3**N):
        # 3進数に分解
        base3_i = []
        while i >= 3:
            tmp = i%3
            i //= 3
            base3_i.append(tmp)
        base3_i.append(i)
        
        # コストと回数を記録
        memo = [0] * M
        cost = 0
        for j, times in enumerate(base3_i):
            # 訪れたことないのはスルー
            if times == 0: continue

            # 来園回数だけ課金
            cost += times*C[j]

            # 動物kiが動物園jにいれば記録
            for ki, l in enumerate(AK[j]): 
                memo[ki] += times*l
        
        # 全て2回以上見ていたら比較
        if all([2 <= xx for xx in memo]): res = min(res, cost)
        
    print(res)

if __name__ == '__main__':
    main()