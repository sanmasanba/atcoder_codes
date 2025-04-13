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
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, Q = map(int, input().split())
    X, Y, Z, W = [0]*Q, [0]*Q, [0]*Q, [0]*Q
    for i in range(Q):
        X[i], Y[i], Z[i], W[i] = map(lambda x: int(x)-1, input().split())
        W[i] += 1

    def check(seq, bit):
        for i in range(Q):
            Ax = seq >> X[i] & 1
            Ay = seq >> Y[i] & 1
            Az = seq >> Z[i] & 1
            Aw = W[i] >> bit & 1
            if (Ax | Ay | Az) != Aw:
                return 0
        return 1
        
    res = 1
    for bit in range(60):
        tmp = 0
        for seq in range(2**N):
            tmp += check(seq, bit)
        res *= tmp
        res %= MOD1000000007
    
    print(res)

if __name__ == '__main__':
    main()