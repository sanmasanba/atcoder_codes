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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, Q = map(int, input().split())
    l = [1]*N
    p2l = [i for i in range(N)]
    res = 0
    for _ in range(Q):
        input_ = input()
        if input_[0] == '1':
            _, p, h = map(lambda x: int(x)-1, input_.split())
            pre_h = p2l[p]
            l[pre_h] -= 1
            if l[pre_h] == 1:
                res -= 1
            p2l[p] = h
            if l[h] == 1:
                res += 1
            l[h] += 1
        elif input_[0] == '2':
            print(res)

if __name__ == '__main__':
    main()