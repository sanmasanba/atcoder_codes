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
    A, B = map(int, input().split())
    l = 0
    r = 1 << 60

    while (r-l) > 10:
        gr = (l + 2*r)//3
        gl = (2*l + r)//3
        ml = A/sqrt(gl+1) + gl * B
        mr = A/sqrt(gr+1) + gr * B
        if ml < mr:
            r = gr
        else:
            l = gl
    
    res = INF
    for g in range(l ,r+1):
        res = min(res, A*10**6/sqrt((g+1)*10**12)+g*B)
    print(res)

if __name__ == '__main__':
    main()