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
    N = int(input())
    S = list(input().strip())
    
    res = deque()
    m = 0
    for i, s in enumerate(S, start=1):
        if m%2 == 0:
            res.append(i)
        else:
            res.appendleft(i)
        m += 1 if s == 'o' else 0
    res = list(res)
    
    print(*res) if m%2==0 else print(*res[::-1])

if __name__ == '__main__':
    main()