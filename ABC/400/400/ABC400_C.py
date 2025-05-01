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

from math import isqrt

#main
def main():
    # intput
    N = int(input())
    
    # x = 2**a * b**2と表されるa, bの組み合わせはいくつかある
    # ここで、bに注目する。b = (1, N^(1/2))の範囲で整数の値を取る
    # この時、bを偶数と奇数で場合分けすると
    # 1) bが偶数
    # b = 2**x * 1
    # 2) bが奇数
    # b = 2**x * c (ただし、cは１からN^(1/2)の奇数)
    # で表すことができる。
    # したがって、2**a < N になる各aについて、bの取りうる奇数の個数を数え上げれば
    # 重複なくかぞえられる
    res = 0
    for a in range(1, 61):
        bb = N//(2**a)
        b = isqrt(bb)
        res += (b+1)//2
    print(res)

if __name__ == '__main__':
    main()