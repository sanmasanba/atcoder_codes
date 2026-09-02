# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

def runlength_encoding(raw: Iterable[T]) -> List[Tuple[T, int]]:
    l, n = 0, len(raw)
    res = []
    while l < n:
        r = l + 1
        while r < n and raw[l] == raw[r]:
            r += 1
        res.append((raw[l], r - l))
        l = r
    return res

# main
def main():
    # intput
    N, T, K = map(int, input().split())
    D = list(map(int, input().split()))

    if N == K:
        print(0)
        return 

    if  K == 0:
        res = 0
        for i in range(N-1):
            res += 0 if abs(D[i] - D[i+1]) <= T else 1
        print(res)
        return

    cumsum = [0]
    for i in range(N-1):
        cumsum.append(cumsum[-1] + (1 if T <= abs(D[i] - D[i+1]) else 0))
    
    res = INF
    for perm in permutations(range(N), K):
        s = ['0'] * N
        for p in perm: s[p] = '1'
        clusters = runlength_encoding(s)
        idx = 0
        tmp = 0
        for (s, le) in clusters:
            l, r = idx, idx+le-1
            if s ==  '0':
                tmp += cumsum[r] - cumsum[l]
            elif s == '1':
                if l == 0:
                    ll = r+1
                else:
                    ll = l-1
                if r == N-1:
                    rr = l-1
                else:
                    rr = r+1
                tmp += 0 if abs(D[rr]-D[ll]) <= T*(rr-ll) else 1
            
            idx += le
        res = min(res, tmp)
    
    print(res)    

if __name__ == '__main__':
    main()
