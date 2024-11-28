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
    
    dp = [[-1]*5 for _ in range(N+1)]
    dp[0][0] = 0

    events = [list(map(int, input().split(' '))) for _ in range(N)]

    pre_time = 0
    for i, event in enumerate(events):
        T, X, A = event
        dtime = T - pre_time
        for pre_hole in range(5):
            if dp[i][pre_hole] == -1:
                continue
            for hole in range(max(0, pre_hole-dtime), min(pre_hole+dtime+1, 5)):
                dp[i+1][hole] = max(dp[i][pre_hole] + (A if hole == X else 0), dp[i+1][hole])
        pre_time = T

    print(max(dp[-1]))

if __name__ == '__main__':
    main()