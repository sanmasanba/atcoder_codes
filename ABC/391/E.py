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
    N = int(input())
    A = input().strip()

    def dfs(l, r):
        if l+1 == r:
            return A[l], 1
        m1 = (2*l+r)//3        
        m2 = (l+2*r)//3
        val1, cnt1 = dfs(l, m1)
        val2, cnt2 = dfs(m1, m2)
        val3, cnt3 = dfs(m2, r)

        # 同じ値が３つあるとき、２つを反転させる
        if val1 == val2 == val3:
            return val1, cnt1+cnt2+cnt3-max(cnt1, cnt2, cnt3)
        # 同じ値が２つあるとき、１つのみ反転させる
        elif val1 == val2:
            return val1, min(cnt1, cnt2)
        elif val1 == val3:
            return val1, min(cnt1, cnt3)
        elif val2 == val3:
            return val2, min(cnt2, cnt3)

    print(dfs(0, 3**N)[1])

if __name__ == '__main__':
    main()