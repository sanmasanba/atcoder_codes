#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')
def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    if Xmi <= x < Xma and Ymi <= y < Yma:
        return False
    else:
        return True

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    MAP = [[-1 for _ in range(N)] for _ in range(N)]
    MAP[0][0] = 0

    move = set()
    for x in range(N):
        if M <= x**2:
            break
        y = int(sqrt(M - x**2))
        if y**2 == M - x**2:
            move.add((x, y))
            move.add((y, x))
            
    Q = deque()
    Q.append((0, 0))
    vecs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            for vecx, vecy in vecs:
                nextx = x + vecx*dx
                nexty = y + vecy*dy
                if is_out_of_range(nextx, nexty, 0, N, 0, N):
                    continue
                if MAP[nexty][nextx] != -1:
                    continue
                MAP[nexty][nextx] = MAP[y][x] + 1
                Q.append((nextx, nexty))
    
    # output
    for m in MAP:
        print(*m)

if __name__ == '__main__':
    main()