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
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    
    # もttも合計が大きいケーキの追加
    que = []
    heappush(que, (-(A[0]+B[0]+C[0]), 0, 0, 0))
    # 追加済みのケーキのメモ
    memo = set([(0, 0, 0)])
    for _ in range(K):
        # 現在最もおいしいケーキ
        score, i, j, k = heappop(que)
        print(-score)

        # 組み合わせ(i+1,, j, k)、(i, j+1, k)、(i, j, k+1)を追加
        # おいしさの合計f(i, j, k) を考えた時
        # f(i, j, k) > f(i+1, j, k) 
        # f(i, j, k) > f(i, j+1, k) 
        # f(i, j, k) > f(i, j, k+1) 
        # から(i+1,, j, k)、(i, j+1, k)、(i, j, k+1)が候補になる
        if i+1 < X and (i+1, j, k) not in memo:
            heappush(que, (-(A[i+1]+B[j]+C[k]), i+1, j, k))
            memo.add((i+1, j, k))
        if j+1 < Y and (i, j+1, k) not in memo:
            heappush(que, (-(A[i]+B[j+1]+C[k]), i, j+1, k))
            memo.add((i, j+1, k))
        if k+1 < Z and (i, j, k+1) not in memo:
            heappush(que, (-(A[i]+B[j]+C[k+1]), i, j, k+1))
            memo.add((i, j, k+1))

if __name__ == '__main__':
    main()