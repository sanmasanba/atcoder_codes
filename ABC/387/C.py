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

def solve(n):
    s = str(n)
    digits = []
    # dp[j][k][l] := i桁目まで決めて、最初の数字がjで
    #                nより小さい(:=k)、leading_zeroかどうか(:=l)
    dp = [[[0]*2 for _ in range(2)] for _ in range(10)]
    # n未満となるもの
    dp[0][1][0] = 1
    # leading_ではなく、n未満となる数
    for i in range(1, int(s[0])):
        dp[i][1][1] = 1
    # 先頭の数
    dp[int(s[0])][0][1] = 1

    #
    for i in range(1, len(s)):
        nxt_dp = [[[0]*2 for _ in range(2)] for _ in range(10)]
        for j in range(10):
            for k in range(2):
                for l in range(2):
                    for nxt_digit in range(10):
                        # leading_zeroかつ前の桁より大きいなら無視
                        if l and j <= nxt_digit:
                            continue
                        # n未満が確定していて、前の桁より小さいとき無視
                        if not k and int(s[i]) < nxt_digit:
                            continue
                        # すでにn未満が確定しているかi+1桁目がs[i]未満ならtrue
                        nxt_k = k or nxt_digit < int(s[i])
                        # leading_zeroでなくなっているか、i+1桁目が0以上ならtrue
                        nxt_l = l or 0 < nxt_digit
                        # if (leading_zeroではなく、i+1桁目が0ではない):
                        #   j_(i+1) = nxt_digit
                        # else:
                        #   j_(i+1) = j
                        nxt_j = nxt_digit if not l and nxt_digit != 0 else j
                        nxt_dp[nxt_j][nxt_k][nxt_l] += dp[j][k][l]
        dp = nxt_dp
    # leading_zeroではない、ものを足し合わせる
    res = 0
    for i in range(10):
        for j in range(2):
            res += dp[i][j][1]
    return res

#main
def main():
    # intput
    L, R = map(int, input().split())
    print(solve(R) - solve(L-1))

if __name__ == '__main__':
    main()