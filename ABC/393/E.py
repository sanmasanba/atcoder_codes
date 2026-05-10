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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    M = max(A)

    # cnt
    cnt = [0] * (M+1)
    for a in A:
        cnt[a] += 1

    ans = [0] * (M+1)
    for i in range(1, M+1):
        c = 0
        # Mまでのiの倍数を調べて、jの登場数ごとに累積和
        for j in range(i, M+1, i):
            c += cnt[j]
        # k個以上であれば、iの倍数はmin(gcd(i, gcd(*))) = iが決まる
        if K <= c:
            for j in range(i, M+1, i):
                ans[j] = i

    for a in A:
        print(ans[a])

if __name__ == '__main__':
    main()