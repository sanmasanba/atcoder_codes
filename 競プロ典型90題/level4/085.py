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
    K = int(input())
    
    res = 0
    for i in range(1, K+1):
        if K < i*i*i:
            break
        if K%i:
            continue
        m = K//i
        for j in range(i, K+1):
            if K < i*j*j:
                break
            if m%j:
                continue
            res += 1
    print(res)

if __name__ == '__main__':
    main()