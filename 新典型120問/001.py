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
    Q = int(input())
    h = []
    b = 0
    res = []
    for q in range(1, Q+1):
        arg = input().split()

        if arg[0] == '1':
            heappush(h, int(arg[1])-b)
        elif arg[0] == '2':
            b += int(arg[1])
        else:
            x = heappop(h)
            res.append(x + b)
    print(*res, sep='\n')

if __name__ == '__main__':
    main()