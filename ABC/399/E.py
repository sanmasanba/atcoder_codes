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
from string import ascii_lowercase

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
    N = int(input())
    S = input().strip()
    T = input().strip()

    # check 
    is_same = True
    check = defaultdict(set)
    for s, t in zip(S, T):
        is_same &= s == t
        check[s].add(t)
    if is_same or 26 <= len(check):
        print(0)
        return
    
    for _, v in check.items():
        if 2 <= len(v): 
            print(-1)
            return
    s_,t_ = '', ''
    for s, t in check.items():
        s_ += s
        t_ += t.pop()
    
    global res
    res = 53
    def dfs(S: str, T: str, cnt: int):
        global res
        if res <= cnt:
            return 
        if S == T:
            res = min(res, cnt)
            return 
        for s, t in zip(S, T):
            if s != t:
                _s = S.replace(s, t)
                dfs(_s, T, cnt+1)
                for c in ascii_lowercase:
                    if c not in S:
                        _s = S.replace(s, c)
                        dfs(_s, T, cnt+1)
                        continue
        return 

    print(dfs(s_, t_, 0))

if __name__ == '__main__':
    main()