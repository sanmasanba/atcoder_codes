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
    S = input()
    N = len(S)

    # dp[p][i] := i番目のマスから、2^p回だけ移動したときのマス
    dp = [[0]*(N+1) for _ in range(33)]
    res = [0]*(N+1)

    for i in range(N):
        match S[i]:
            case 'R':
                dp[0][i] = i+1
            case 'L':
                dp[0][i] = i-1
    
    # dp[p+1][i] <- dp[p][dp[p][i]]
    # iマス目にいるとき、そこから2^p回移動する 
    for p in range(32):
        for i in range(N):
            dp[p+1][i] = dp[p][dp[p][i]]
    
    for i in range(N):
        res[dp[32][i]] += 1
    print(*res[:N])

if __name__ == '__main__':
    main()