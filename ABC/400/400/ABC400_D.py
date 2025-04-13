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

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

#main
def main():
    # intput
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]
    A, B, C, D = map(lambda x: int(x)-1, input().split())
    
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cost = [[INF]*W for _ in range(H)]
    queue = deque()
    s = (A, B)
    cost[A][B] = 0
    queue = []
    heappush(queue, (0, s))

    while queue:
        current_dist, current_pos = heappop(queue)
        (x, y) = current_pos

        if current_dist > cost[x][y]:
            continue

        for dx, dy in d:
            nx, ny, nxx, nyy = x+dx, y+dy, x+dx*2, y+dy*2

            if not is_out_of_range(nx, ny, 0, H, 0, W):
                if  S[nx][ny] == '.' and cost[x][y] < cost[nx][ny]:
                    cost[nx][ny] = cost[x][y]
                    heappush(queue, (cost[nx][ny], (nx, ny)))
                elif S[nx][ny] == '#' and cost[x][y] + 1 < cost[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 1
                    heappush(queue, (cost[nx][ny], (nx, ny)))
            if not is_out_of_range(nxx, nyy, 0, H, 0, W):
                if  (S[nxx][nyy] == '#' or S[nx][ny] == '#') and cost[x][y] + 1 < cost[nxx][nyy]:
                    cost[nxx][nyy] = cost[x][y] + 1
                    heappush(queue, (cost[nxx][nyy], (nxx, nyy)))
        
    print(cost[C][D])

if __name__ == '__main__':
    main()