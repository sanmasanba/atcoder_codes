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
    N, H, W = map(int, input().split(' '))
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        if max(H,W) < max(a, b):
            continue
        
        A.append(a)
        B.append(b)
    N = len(A)
    if N == 0:
        print('No')
        return
    
    global res
    res = False
    grid = [[1]*(W+2) for _ in range(H+2)]
    for i in range(1, H+1):
        for j in range(1, W+1):
            grid[i][j] = 0

    def check(h, w, A, B):
        for a in range(A):
            for b in range(B):
                if grid[h+a][w+b]:
                    return False
        return True
    
    def put(h, w, A, B):
        for a in range(A):
            for b in range(B):
                grid[h+a][w+b] = 1
                    
    def clear(h, w, A, B):
        for a in range(A):
            for b in range(B):
                grid[h+a][w+b] = 0
    
    def dfs(l, used, mask):
        global res        
        if all(used) or res:
            res = True
            return
        
        def process(h, w, a, b, mask):
            put(h, w, a, b)
            used[i] = True
            dfs(l, used, mask)
            used[i] = False
            clear(h, w, a, b)
            
        for i, tile in enumerate(l):
            if used[i]: continue
            
            a, b = A[tile], B[tile]
            if mask: a, b = b, a
            for h in range(1, H-a+2):
                for w in range(1, W-b+2):
                     if (grid[h-1][w] and grid[h][w-1] and 
                         grid[h-1][w-1] and check(h, w, a, b)):
                        process(h, w, a, b, 0)
                        process(h, w, a, b, 1)
    
    for mask1 in range(1, 1<<N):
        l = []
        area = 0
        for i in range(N):
            if mask1 >> i & 1:
                l.append(i)
                area += A[i]*B[i]
        if area != H*W: continue
        dfs(l, [False]*len(l), 0)
        if res: break
        dfs(l, [False]*len(l), 1)
        if res: break
        
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()