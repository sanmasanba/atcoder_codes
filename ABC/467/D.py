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

def solve(px, py, qx, qy, rx, ry, sx, sy):
    # 1) おなじ垂直二等分線を共有しているならtrue
    f1 = (px-qx)*(ry-sy) == (rx-sx)*(py-qy)
    f2 = (-(ry - sy)*((px*px - qx*qx) + (py*py - qy*qy)) 
          == -(py - qy)*((rx*rx - sx*sx) + (ry*ry - sy*sy)))
    if f1 and f2:
        return True
    # 2) 傾きが異なるならtrue
    elif not f1:
        return True
    else:
        return False

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
        if solve(px, py, qx, qy, rx, ry, sx, sy):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()