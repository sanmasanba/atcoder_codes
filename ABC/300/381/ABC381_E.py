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
    # intput
    N, Q = map(int, input().split(' '))
    S = list(input())
    # '1', '2', '/'の登場位置を記録
    pos_1, pos_2, pos_thresh = [], [], []
    for i, s in enumerate(S):
        if s == '1':
            pos_1.append(i)
        elif s == '2':
            pos_2.append(i)
        else:
            pos_thresh.append(i)

    res = []
    for _ in range(Q):
        L, R = map(int, input().split(' '))
        L -= 1

        def solve(length):
            # 長さが0の時、'/'が範囲内にあるかを判定
            if length == 0:
                j = bisect_left(pos_thresh, L)
                if len(pos_thresh) <= j:
                    return False
                return pos_thresh[j] < R
            
            # Lから見てlength個の'1'をとれるか判定
            i = bisect_left(pos_1, L)
            if len(pos_1) <= i + length - 1:
                return False
            # '1'を取った直後の'/'が範囲内か判定
            j = bisect_left(pos_thresh, pos_1[i + length - 1])
            if len(pos_thresh) <= j:
                return False
            # '/'の位置からlength個の'2'がとれるか判定
            k = bisect_left(pos_2, pos_thresh[j])
            if len(pos_2) <= k + length - 1:
                return False
            # 作成した11/22文字列が、[L, R]の範囲内か判定
            return pos_2[k + length - 1] < R

        # 長さ2*m+1以上の部分列があるかを判定
        ok, ng = -1, N+1
        while ok + 1 < ng:
            m = (ok + ng)//2
            if solve(m):
                ok = m
            else:
                ng = m
        res .append(0 if ok == -1 else 2*ok+1)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()