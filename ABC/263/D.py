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
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    l_cumsum = [0] + list(accumulate(A))
    r_cumsum = [0] + list(accumulate(A[::-1]))
    
    l_memo = [INF]*(N+1)
    r_memo = [INF]*(N+1)
    l_memo[0]=INF
    r_memo[-1]=INF
    for i in range(N):
        l_memo[i+1] = min(l_memo[i], L*(i+1), l_cumsum[i+1]+L*i)
    for i in range(N):
        r_memo[N-(i+1)] = min(r_memo[N-i], R*(i+1), r_cumsum[i+1]+R*i)
    print(r_cumsum)
    print(l_memo)
    print(r_memo)

if __name__ == '__main__':
    main()