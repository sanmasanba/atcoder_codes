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

# main
def main():
    # intput
    N, C = map(int, input().split())

    # 1) bit が 0 の時と 1 の時を仮定する
    f0, f1 = 0, (1 << 30) - 1

    # 2) それぞれ個別に処理を考える
    for _ in range(N):
        T, A = map(int, input().split())
        match T:
            case 1:
                f0, f1 = f0 & A, f1 & A
            case 2:
                f0, f1 = f0 | A, f1 | A
            case 3:
                f0, f1 = f0 ^ A, f1 ^ A
            case _:
                raise
        # 3) C の現在の bit に対して mask を適用
        C = (C & f1) | (~C & f0)
        C &= (1 << 30) - 1

        print(C)
            

if __name__ == '__main__':
    main()
