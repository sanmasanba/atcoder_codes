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
    S = [list(input()) for _ in range(N)]

    other2a = 0
    b2other = 0
    b2a = 0
    other2other = 0
    
    res = 0
    for i in range(N):
        a_flg = S[i][-1] == 'A'
        b_flg = S[i][0] == 'B'
        for j in range(len(S[i])-1):
            if S[i][j]=='A' and S[i][j+1]=='B':
                res += 1
        if a_flg and b_flg:
            b2a += 1
        elif a_flg:
            other2a += 1
        elif b_flg:
            b2other += 1
        else:
            other2other += 1
    
    flg = False
    for i in range(N):
        # 先頭は可能ならbを使わない
        if i == 0:
            if 0 < other2a:
                other2a -= 1
                flg = True
            elif 0 < b2a:
                b2a -= 1
                flg = True
            else:
                break
            continue
        
        if flg:
            if 0 < b2a:
                b2a -= 1
                res += 1
            elif 0 < b2other:
                b2other -= 1
                res += 1
                flg = False
            elif other2a:
                other2a -= 1
            elif 0 < other2other:
                other2other -= 1
                flg = False
        else:
            if 0 < other2a:
                other2a -= 1
                flg = True
            elif 0 < b2a:
                b2a -= 1
                flg = True
            elif other2other:
                other2other -= 1
                flg = False
            elif 0 < b2other:
                b2other -= 1       

    print(res) 

if __name__ == '__main__':
    main()