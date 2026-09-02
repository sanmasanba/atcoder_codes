# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# 考察
# 周期性を考えると、先頭になる候補はN通りしかない
# 0 から順にシミュレートしても、O(N)
# (simu)
# 1) X >= sum(W) なら、w = X//sum(W)周する
# 2-1) X -= w * sum(W) について周期性を見る
# 2-2) i番目から何個めでXを超えるかは累積和をもって二分探索すればO(logN)
# -> O(NlogN)
# 3) クエリはO(1)で回答できる

# main
def main():
    # intput
    N, Q, X = map(int, input().split())
    W = list(map(int, input().split()))
    cumsum = [0] + list(accumulate(W + W))

    w = sum(W)
    a = X//w
    X %= w
    keys = []
    memo = defaultdict(int)
    s = 0
    while s not in memo:
        keys.append(s)
        memo[s] = a * N

        if 0 < X:
            ok = 2*N - 1
            ng = s - 1
            while ok - ng > 1:
                mi = (ok + ng) // 2
                if X <= (cumsum[mi+1] - cumsum[s]):
                    ok = mi
                else:
                    ng = mi
            memo[s] += ok + 1 - s
            s = (ok + 1) % N
    idx = keys.index(s)
    head = keys[:idx]
    body = keys[idx:]

    for _ in range(Q):
        key = int(input()) - 1
        if key < len(head):
            print(memo[head[key]])
        else:
            print(memo[body[(key - len(head))%len(body)]])

if __name__ == '__main__':
    main()
