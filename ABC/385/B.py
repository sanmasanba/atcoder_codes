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
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = [list(input()) for _ in range(H)]
    T = input()
    
    move2d = {'U':0, 'D':1, 'L':2, 'R':3}
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    res = set()
    for t in T:
        dh, dw = d[move2d[t]]
        nx = X+dh
        ny = Y+dw
        if S[nx][ny] == '#':
            pass
        else:
            if S[nx][ny] == '@':
                res.add((nx, ny))
            X, Y = nx, ny
    print(X+1, Y+1, len(res))

if __name__ == '__main__':
    main()