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

import math

# get angle of (x, y) from x-axis based on i-th point
def get_angle(x, y):
    rad = max(-1, min(1, x / sqrt(x * x + y * y)))
    thete = math.acos(rad) * 180 / pi
    if 0 <= y:
        return thete   
    else:
        return 360 - thete

# get angle between two points
def get_angle2(p1, p2):
    res = abs(p1 - p2)
    if 180 <= res:
        return 360 - res
    return res

#main
def main():
    # intput
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for j in range(N):
        # argsort based on XY[j]
        sorted_XY = []
        for i in range(N):
            if i == j:
                continue
            dx, dy = XY[i][0] - XY[j][0], XY[i][1] - XY[j][1]
            sorted_XY.append(get_angle(dx, dy))    
        sorted_XY.sort()

        # search for the maximum angle for all points
        for i in range(len(sorted_XY)):
            target = sorted_XY[i] + 180
            if 360 <= target:
                target -= 360
            pos = bisect_left(sorted_XY, target)

            # only two points that are candidates
            cnd1 = pos % len(sorted_XY)
            cnd2 = (pos + len(sorted_XY) - 1) % len(sorted_XY)
            cnd1_angle = get_angle2(sorted_XY[i], sorted_XY[cnd1])
            cnd2_angle = get_angle2(sorted_XY[i], sorted_XY[cnd2])
            res = max(res, cnd1_angle, cnd2_angle)
    print(res)

if __name__ == '__main__':
    main()