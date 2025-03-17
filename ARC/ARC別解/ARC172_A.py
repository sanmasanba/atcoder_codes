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

#main
def main():
    # 大きさ (2 の r 乗) * (2 の r 乗) 以上の渡すべきチョコの合計面積を返す関数
    def TotalArea(H, W, N, A, r):
        Area = 0
        for i in A:
            if i >= r:
                Area += (2 ** i) * (2 ** i)
        return Area

    # Step 1. 入力
    H, W, N = map(int, input().split())
    A = list(map(int, input().split()))

    # Step 2. 大きさ 1, 2, 4, ..., (2 の 25 乗) について、条件を満たしているかをチェック
    for r in range(0, 26):
        LimitH = H // (2 ** r) # H / (2 の r 乗) の切り捨て
        LimitW = W // (2 ** r) # W / (2 の r 乗) の切り捨て
        LimitArea = LimitH * LimitW * (2 ** r) * (2 ** r) # 面積の上限

        # 渡すべき合計面積と比較する
        ActualArea = TotalArea(H, W, N, A, r)

        # もし上限を超えていたら、答えは即 No
        if ActualArea > LimitArea:
            print("No")
            sys.exit(0)

    # Step 3. もし全条件を満たせば Yes を出力
    print("Yes")

if __name__ == '__main__':
    main()