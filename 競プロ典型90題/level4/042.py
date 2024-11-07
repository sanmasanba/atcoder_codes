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

#main
def main():
    # intput
    K = int(input())
    
    if K%9 != 0:
        print(0)
        return
    
    dp = [0] * 100010
    dp[0] = 1

    # 桁ごとの総和をiとする
    for i in range(1, K+1):
        # 先頭の数の最大値を指定する
        top_seq = min(i, 9)
        # 先頭の数がjだった時、桁和がKとなるのは先頭桁以外の桁和がK-jとなるとき
        for j in range(1, top_seq+1):
            dp[i] = (dp[i] + dp[i - j]) % (10**9+7)

    print(dp[K]) 

if __name__ == '__main__':
    main()