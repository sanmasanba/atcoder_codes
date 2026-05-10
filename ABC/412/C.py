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

def solver():
    N = int(input())
    S = list(map(int, input().split()))
    s, l = S[0], S[-1]
    res = [s]
    S = sorted(S)
    while 1:
        idx = bisect_right(S, 2*res[-1])
        # 自分自身しか倒せず、それが最後のドミノではない
        if S[idx-1] == res[-1] and S[idx-1] < l:
            print(-1)
            return
        # 今倒せる最大のドミノ
        else:
            res.append(S[idx-1])
        # 最大のドミノが最後のドミノより大きいとき
        if l <= res[-1]:
            print(len(res))
            return

#main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solver()

if __name__ == '__main__':
    main()