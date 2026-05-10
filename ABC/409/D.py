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
MOD998 = 998244353
MOD1e7 = 1000000007

def solver():
    N = int(input())
    S = input().strip()
    
    for i in range(N-1):
        if ord(S[i]) > ord(S[i+1]):
            res = S[:i]
            for j in range(i+1, N):
                if ord(S[i]) >= ord(S[j]):
                    res += S[j]
                else:
                    res += S[i]
                    res += S[j:]
                    break
            if len(res) < N: res += S[i]
            print(res)
            return
    print(''.join(S))

#main
def main():
    # intput
    N = int(input())
    for _ in range(N):
        solver()

if __name__ == '__main__':
    main()