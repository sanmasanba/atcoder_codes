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
MOD998 = 998244353
MOD1e7 = 1000000007

#main
def main():
    # intput
    S = input().strip()
    T = input().strip()

    S_dict = defaultdict(list)
    for i, s in enumerate(S):
        S_dict[s].append(i)
    idx = 0
    idxs = 0
    for t in T:
        if t not in S_dict:
            print(-1)
            return
        _idx = bisect_left(S_dict[t], idx)
        if len(S_dict[t]) <= _idx:
            _idx = bisect_left(S_dict[t], 0)
            idxs += 1
        elif len(S) <= S_dict[t][_idx]+1:
            idxs += 1
        idx = (S_dict[t][_idx] + 1)%len(S)
        # print(idx, idxs)

    print(idxs*len(S) + idx)

if __name__ == '__main__':
    main()