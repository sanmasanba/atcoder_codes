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
    N, M = map(int, input().split())
    KA = []
    for _ in range(M):
        K, *A = list(map(int, input().split()))
        KA.append([K, A])
    B = {b:i for i, b in (enumerate(map(int, input().split())))}
    
    res = [0]*N
    for ka in KA:
        K, A = ka
        tmp = 0
        for a in A:
            tmp = max(tmp, B[a])
        res[tmp] += 1
    ans = 0
    for r in res:
        ans += r
        print(ans)     

if __name__ == '__main__':
    main()