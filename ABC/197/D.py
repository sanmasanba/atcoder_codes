#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, \
    factorial, atan2, sin, cos, radians
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
    x00, y00 = map(int, input().split(' '))
    x05, y05 = map(int, input().split(' '))

    # 中点の座標    
    qx, qy = (x00+x05)/2, (y00+y05)/2
    # 中点からのベクトル
    v0x, v0y = x00 - qx, y00 - qy

    # 回転分を求める
    s = sin(radians(360/N))
    c = cos(radians(360/N))
    v1x, v1y = v0x*c-v0y*s, v0x*s+v0y*c

    print(qx+v1x, qy+v1y)

if __name__ == '__main__':
    main()