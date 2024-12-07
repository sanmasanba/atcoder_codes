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
    N = int(input())
    
    # 奇数は2で因数分解できないので、常に0
    if N%2:
        print(0)
    else:
        n = N//2
        # f(N) = 2**n * n! になる
        # 2**nは、末尾が0にならないので無視できる
        # ルジャンドルの定理を用いて、2と5の因数の数を求める
        def f(p, n):
            P = p
            cnt = 0
            while p <= n:
                cnt += n//p
                p *= P
            return cnt
        # 10 = 2*5 より、min(2の因数の数+n, 5の因数の数)
        res = min(f(2, n)+n, f(5, n))
        print(res)

if __name__ == '__main__':
    main()