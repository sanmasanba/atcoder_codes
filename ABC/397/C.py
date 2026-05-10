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
    A = list(map(int, input().split()))
    
    l_set = set()
    r_set = set()
    lcnt = [0]
    rcnt = [0]
    for i in range(N):
        l, r = A[i], A[-1-i]
        if l not in l_set:
            lcnt.append(lcnt[-1]+1)
        else:
            lcnt.append(lcnt[-1])
        if r not in r_set:
            rcnt.append(rcnt[-1]+1)
        else:
            rcnt.append(rcnt[-1])
        l_set.add(l)
        r_set.add(r)

    res = -1
    for i in range(N-1):
        l, r = lcnt[i+1], rcnt[-i-2]
        res = max(res, l+r)
    print(res)

if __name__ == '__main__':
    main()