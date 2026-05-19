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
    N = int(input())
    S = list(map(int, input().strip()))
    
    buf = [0] * (N+1)
    for i, s in enumerate(S, start=1):
        buf[i] = buf[i-1] + i * s
    buf = buf[1:]

    tmp = 0
    res = []
    for r in buf[::-1]:
        tmp += r
        res.append(str(tmp%10))
        tmp //= 10
    if tmp != 0:
        res.append(str(tmp%10))
    print("".join(res[::-1]))

if __name__ == '__main__':
    main()