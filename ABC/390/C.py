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
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    left = -1
    right = -1
    top = -1
    low = -1
    for j in range(W):
        for i in range(H):    
            if S[i][j] == '#':
                left = j
                break
        if left != -1:
            break
    for j in range(W-1, -1, -1):
        for i in range(H):    
            if S[i][j] == '#':
                right = j
                break
        if right != -1:
            break
    for i in range(H):    
        for j in range(W):
            if S[i][j] == '#':
                top = i
                break
        if top != -1:
            break
    for i in range(H-1, -1, -1):    
        for j in range(W):
            if S[i][j] == '#':
                low = i
                break
        if low != -1:
            break

    if (left, right, top, low) == (-1, -1, -1, -1):
        print('Yes')
        return
    
    for i in range(H):
        for j in range(W):
            if top <= i <= low and left <= j <= right:
                if S[i][j] == '.':
                    print('No')
                    return
            else:
                if S[i][j] == '#':
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()