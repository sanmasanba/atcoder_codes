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
    S =  input().strip()
    cnt = 0
    res = 0
    for c in S:
        if cnt%2 and c == 'i':
            res += 1
        elif not cnt%2 and c == 'o':
            res += 1
        else:
            cnt += 1
    if S[-1] == 'i':
        res += 1
    print(res)

if __name__ == '__main__':
    main()