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

def solve():
    S = list(input().strip())
    tmp = Counter(S)
    cnt = sorted([(cnt, c) for (c, cnt) in tmp.items()], key=lambda x: -x[0])
    D = ''
    for (cn, c) in cnt: D += c * cn
    N = len(D)
    M = N//2+1 if N%2 else N//2
    buf = [''] * M
    for i, s in enumerate(D):
        if buf[i%M] and buf[i%M][-1] == s:
            print('No')
            return
        buf[i%M] += s
    print('Yes')
    print(''.join(buf))

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()