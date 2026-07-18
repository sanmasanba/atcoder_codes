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
    A, B, C, D, E, F, X = map(int, input().split())
    t = X//(A+C)*B*A + min(max(0, X%(A+C)), A)*B
    a = X//(D+F)*E*D + min(max(0, X%(D+F)), D)*E
    
    if t < a:
        print('Aoki')
    elif a < t:
        print('Takahashi')
    else:
        print('Draw')

if __name__ == '__main__':
    main()