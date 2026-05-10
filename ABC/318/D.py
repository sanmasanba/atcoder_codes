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

def generate(n, N):
    res = []
    for bits in combinations(range(N), n):
        num = 0
        for bit in bits:
            num |= 1 << bit
        res.append(num)
    return res

#main
def main():
    # intput
    N = int(input())
    G = [[-1]*(N) for _ in range(N)]
    for i in range(N-1):
        D = map(int, input().split(' '))
        for j, dij in enumerate(D, start=i+1):
            G[i][j] = dij
    
    # bitdp[i] := iに対応するエッジが接続されているときの総和
    dp = [0] * 2**N
    edges = generate(2, N)
    for num in edges:
        idx = [i for i in range(N) if num >> i & 1]
        i, j = idx
        dp[num] = G[i][j]

    for bits in range(2, N+1, 2):
        for a in generate(bits, N):
            for b in edges:
                ab: int = a | b
                if ab.bit_count() == bits+2:
                    dp[ab] = max(dp[ab], dp[a]+dp[b])

    print(max(dp))

if __name__ == '__main__':
    main()