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
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # grundy数を求める
    # Biの最大値は、W=50, B=50のときにW'=(50*51)//2 = 1275をBに足して
    # B = 50 + 1275 = 1325
    grundy_num = [[0] * 1500 for _ in range(60)]
    for w in range(51):
        for b in range(1326):
            memo = [0] * 2000
            # 白石が1つ以上なら遷移可能
            if 1 <= w:
                memo[grundy_num[w-1][b+w]] = 1
            # 青石が2つ以上なら遷移可能
            if 2 <= b:
                for k in range(1, b//2+1):
                    memo[grundy_num[w][b-k]] = 1
            # mexを求める
            for k in range(2000):
                if memo[k] == 0:
                    grundy_num[w][b] = k
                    break

    # grundy数の性質から、res = 0なら後手、res != 0なら先手が必勝
    res = 0
    for i in range(N):
        res ^= grundy_num[W[i]][B[i]]
    print('Second' if res == 0 else 'First')

if __name__ == '__main__':
    main()