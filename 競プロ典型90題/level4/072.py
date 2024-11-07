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

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    if Xmi <= x < Xma and Ymi <= y < Yma:
        return False
    else:
        return True

def solve(MAP, x, y, sx, sy, H, W, dist):
    global ans
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not is_out_of_range(nx, ny, 0, W, 0, H) and MAP[ny][nx] == '.':
            if nx == sx and ny == sy:
                ans = max(ans, dist+1)
            elif (nx, ny) not in seen: 
                seen.add((nx, ny))
                solve(MAP, nx, ny, sx, sy, H, W, dist+1)
                seen.remove((nx, ny))

#main
def main():
    # intput
    H, W = map(int, input().split(' '))
    MAP = [list(input()) for _ in range(H)]

    global seen
    global ans
    ans = -1
    for sy in range(H):
        for sx in range(W):
            if MAP[sy][sx] == '#':
                continue
            seen = set([(sx, sy)])
            solve(MAP, sx, sy, sx, sy, H, W, 0)
            seen.remove((sx, sy))
            print(ans)    
    
    print(ans if ans > 3 else -1)

if __name__ == '__main__':
    main()