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
    # 垂直二等分線の式で整理： Ax + By = C
    # d(P, (x, y)) = d(Q, (x, y))
    # => (x - Px)^2 + (y - Py)^2 = (x - Qx)^2 + (y - Qy)^2
    # => x^2-2xPx+Px^2+y^2-2yPy+Py^2 = x^2-2xQx+Qx^2+y^2-2yQy+Qy^2
    # => - 2xPx + Px^2 - 2yPy + Py^2 = - 2xQx + Qx^2 - 2yQy + Qy^2
    # => 2(Qx - Px)x + 2(Qy - Py) = (Qx^2 + Qy^2) - (Px^2 + Py^2)
    a1, b1, c1 = 2*(qx - px), 2*(qy - py), (qx*qx + qy*qy) - (px*px + py*py)
    a2, b2, c2 = 2*(sx - rx), 2*(sy - ry), (sx*sx + sy*sy) - (rx*rx + ry*ry)

    # 1) 傾きが異なるとき、どこかで交差する
    if a1 * b2 != a2 * b1:
        return True

    # 2) 平行な時、同じ直線なら交差、そうでなければ交差しない
    return (a1*c2 == a2*c1) and (b1*c2 == b2*c1)

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