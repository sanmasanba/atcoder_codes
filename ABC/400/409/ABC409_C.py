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
    N, L = map(int, input().split())
    D = list(map(int, input().split()))
    if L%3:
        print(0)
        return
    
    memo = {i:0 for i in range(L)}
    memo[0] = 1
    pos = 0
    for d in D:
        pos = (pos + d) % L
        memo[pos] += 1
    
    res = 0
    for i in range(L//3):
        ii, iii = i+L//3, i+2*L//3
        res += memo[i] * memo[ii] * memo[iii]
    print(res)

if __name__ == '__main__':
    main()