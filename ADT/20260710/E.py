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

# main
def main():
    # intput
    K = int(input())
    S = list(input().strip())
    T = list(input().strip())
    
    if abs(len(S) - len(T)) > 1:
        print('No')
        return
    
    s_idx = 0
    t_idx = 0
    flg = False
    while t_idx < len(T) and s_idx < len(S):
        if S[s_idx] != T[t_idx]:
            if flg: 
                print('No')
                return
            if len(T) < len(S):
                s_idx += 1
            elif len(S) < len(T):
                t_idx += 1
            else:
                s_idx += 1
                t_idx += 1
            flg = True
            if (s_idx < len(S) 
                and t_idx < len(T) 
                and S[s_idx] != T[t_idx]):
                print('No')
                return
        s_idx += 1
        t_idx += 1
    print('Yes')

if __name__ == '__main__':
    main()