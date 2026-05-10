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
    N = int(input())
    need, Z = [], []
    sum_z = 0
    curr_z = 0
    for _ in range(N):
        x, y, z = map(int, input().split(' '))
        sum_z += z
        if y < x:
            curr_z += z
            continue
        need.append((x+y+1)//2-x)
        Z.append(z)

    if sum_z < 2*curr_z:
        print(0)
        return

    need_z = (sum_z+1)//2 - curr_z    
    dp = [[INF]*(need_z+1) for _ in range(len(Z)+1)]
    for i in range(len(Z)+1): dp[i][0] = 0

    for i, p in enumerate(need):
        z = Z[i]
        for base in range(need_z+1):
            dp[i+1][base] = min(dp[i][base], dp[i+1][base])
            j = min(base+z, need_z)
            dp[i+1][j] = min(dp[i][base]+p, dp[i+1][j])

    print(dp[-1][-1])

if __name__ == '__main__':
    main()