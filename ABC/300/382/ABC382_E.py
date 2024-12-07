#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N, X = map(int, input().split(' '))
    P = list(map(lambda x: int(x)/100, input().split(' ')))
    
    dp = [0]*(N+1)
    dp[0] = 1

    res = 0
    cnt = 1
    while dp[-1] < 1-1e-7:
        tmp = [0]*(N+1)
        for i, d in enumerate(dp):
            for p in P:
                tmp[i] += d*(1-p)
                tmp[min(i+1, N)] += d*p
        res += cnt*tmp[-1]
        cnt += 1
        dp = tmp[:]
        print(dp)
    print(res)

if __name__ == '__main__':
    main()