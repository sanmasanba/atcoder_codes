#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop, heapify
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

import math

#main
def main():
    # intput
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A.sort(reverse=True)

    # 総和がK以下なら、K回乗ることができる
    if sum(A) <= K:
        res = 0
        for a in A: res += ((a+1)*a)//2
        print(res)
        return
    
    # 乗った回数がK以下となる最大のrを求める
    l = 0
    r = 2*10**9+1
    while l+1 < r:
        m = (l+r)//2
        cnt = 0
        for a in A:
            if a <= m:
                break
            cnt += a - m
        
        if cnt >= K:
            l = m
        else:
            r = m

    # 貪欲にrになるまで乗る
    res = 0
    ride = 0
    for a in A:
        if a <= r:
            break
        ride += a - r
        res += ((a-r)*(a + r + 1))//2
    
    # 残りはrを乗る
    res += (K - ride) * r
    print(res)

if __name__ == '__main__':
    main()