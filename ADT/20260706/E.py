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

# main
def main():
    # intput
    N, K, X = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    
    # 最悪ケースを考える
    # 1) 小さいほうからK個までがすべてアルコールとする
    mi = A[:min(N, K)]
    # 2) 大きいほう[K:]に含まれてないけど全部飲んだとする
    res = N-K
    cnt = 0
    # 3) 大きいほうから攻めていく
    for a in mi[::-1]:
        res += 1
        cnt += a
        if X <= cnt:
            print(res)
            return
    print(-1)

if __name__ == '__main__':
    main()