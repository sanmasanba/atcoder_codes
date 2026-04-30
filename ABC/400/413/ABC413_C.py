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
    Q = int(input())
    A = [[0, 0, 0, 0, -1]]
    cursor = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append([A[-1][1],                     # 左端
                      A[-1][1]+query[1],            # 右端
                      A[-1][2]+query[1]*query[2],   # 右端までの総和
                      query[1],                     # 個数
                      query[2]])                    # 要素
        elif query[0] == 2:
            k = query[1]
            l, r = cursor, cursor + k
            l_idx = bisect_left(A, l, key=lambda x: x[1])
            r_idx = bisect_left(A, r, key=lambda x: x[1])
            # print(l_idx, r_idx)
            l_sum = A[l_idx][2] - A[l_idx][4] * (A[l_idx][1] - l)
            r_sum = A[r_idx][2] - A[r_idx][4] * (A[r_idx][1] - r)
            print(r_sum-l_sum)
            cursor = r

if __name__ == '__main__':
    main()