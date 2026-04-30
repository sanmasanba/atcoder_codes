# library
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
MOD998 = 998244353
MOD1e7 = 1000000007

def ranked(A):
    tmp = [(a, i) for i, a in enumerate(A)]
    tmp.sort(reverse=True)
    r = [0]*len(A)
    for rank, (_, i) in enumerate(tmp): r[i] = rank+1
    return r

# main
def main():
    # intput
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X = list(sorted(list(set(X))))

    SUB = [X[i+1]-X[i] for i in range(len(X)-1)]
    r = ranked(SUB)

    res = 0
    tmp = []
    for i, x in enumerate(X):
        tmp.append(x)
        if i < len(X)-1 and r[i] < M:
            res += tmp[-1] - tmp[0]
            tmp = []
    if tmp:
        res += tmp[-1] - tmp[0]
        tmp = []
    print(res)    

if __name__ == '__main__':
    main()