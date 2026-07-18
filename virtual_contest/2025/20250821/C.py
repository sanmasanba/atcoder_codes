# library
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

# main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    S = list(input().strip())
    
    # Eを固定して、MとEの組み合わせを列挙
    M_memo = [0, 0, 0]
    ME_memo = [[0 for _ in range(9)]]
    for i, s in enumerate(S):
        tmp = ME_memo[-1][:]
        if s == 'M':
            M_memo[A[i]] += 1
        elif s == 'E':
            for j in range(3):
                tmp[3*A[i]+j] += M_memo[j]
        ME_memo.append(tmp)

    # mex(a, b, c)
    def ret_mex(a, b, c):
        tmp = set([a, b, c])
        for i in range(4):
            if i not in tmp: return i

    # Xの位置に限りMEXを計算する
    res = 0
    for i in range(N):
        if S[i] == 'X':
            tmp = ME_memo[i+1]
            for j in range(9):
                a = j//3
                b = j%3
                res += ret_mex(a, b, A[i]) * tmp[j]
    print(res)

if __name__ == '__main__':
    main()