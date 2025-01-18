#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, isqrt
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
    R = int(input())
    
    x = 500
    y = 500
    R *= 1000

    x_start = (x-R)//1000
    x_end = (x+R)//1000

    res = 0
    for i in range(x_start, x_end+1):
        y_2 = pow(R, 2) - pow(x - i*1000, 2)
        if y_2 >= 0:
            root_y = isqrt(y_2)
            y_max = int((x + root_y)//1000)
            y_min = int(((x - root_y - 1)//1000))
            if (x - root_y - 1) < 0:
                y_min += 1
            if i == 0:
                continue

            res += y_max - y_min
    print(res)

if __name__ == '__main__':
    main()