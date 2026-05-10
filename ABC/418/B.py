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
    if len(S) <= 2:
        print(0)
        return

    res = 0
    for i in range(len(S)-1):
        if S[i] != 't': continue
        for j in range(i+2, len(S)):
            if S[j] != 't': continue
            cnt = 0
            for k in range(i, j+1):
                if S[k] == 't':
                    cnt += 1
            res = max(res, (cnt-2)/(j-i-1))
    print(res)

if __name__ == '__main__':
    main()