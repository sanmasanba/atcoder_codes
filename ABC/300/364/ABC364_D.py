#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = []
    for _ in range(Q):
        b, k = map(int, input().split(' '))
        B.append([b, k])

    A.sort()
    for b, k in B:
        # 下限と上限を設定
        lo, hi = -1, 10**9
        # 点bを中心としてb±miの範囲にある点の数を数える。
        while lo + 1 < hi:
            mi = (lo+hi)//2
            # [b-mi, b+mi]の範囲にある点の数を数える
            c = bisect_right(A, b+mi) - bisect_left(A, b-mi)
            # 数が多いとき、bを中心としてより狭い範囲
            if c >= k:
                hi = mi
            # 数が少ないとき、bを中心としてより大きい範囲
            else:
                lo = mi
        print(hi)

if __name__ == '__main__':
    main()