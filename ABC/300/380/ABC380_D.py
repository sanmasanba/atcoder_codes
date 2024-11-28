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

def solve(N, k):
    global S
    global block
    s = bisect_left(block, k)
    if k <= N:
        return S[k-1], 0

    k = k-block[s-1]
    c, cnt = solve(N, k)
    return c, cnt+1

#main
def main():
    # intput
    global S
    S = list(input())
    Q = int(input())
    K = list(map(int, input().split(' ')))
    
    N =len(S)
    global block
    block = [N]
    pos = N
    while block[-1] < max(K):
        block.append(block[-1]+block[-1])

    for k in K:
        if k <= N:
            print(S[k-1], end=' ')
            continue
        c, cnt = solve(N, k)
        if cnt%2:
            if 65 <= ord(c) <= 90: print(c.lower(), end=' ')
            else: print(c.upper(), end=' ')
        else:
            print(c, end=' ')
    

if __name__ == '__main__':
    main()