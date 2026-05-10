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

MOD = 998244353

def mod_inverse(a, p):
    return pow(a, p-2, p)

#main
def main():
    # input
    N, K = map(int, input().split(' '))
    
    # dp[i] = i回目のスワップで一番左に黒いボールがある確率
    dp = [0] * (K+1)
    dp[0] = 1
    
    M = mod_inverse(N**2, MOD)
    p = 2*(N-1)%MOD*M%MOD
    q = 2*M%MOD
    
    for k in range(K):
        dp[k+1] = ((dp[k]*(1-p))%MOD + ((1-dp[k])%MOD)*q%MOD)%MOD

    u = (N+2)*mod_inverse(2, MOD)%MOD
    print((dp[-1] + u * (1-dp[-1]))%MOD)

if __name__ == '__main__':
    main()