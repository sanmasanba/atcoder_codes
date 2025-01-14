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
MOD = 1000000007

#main
def main():
    # intput
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    def calc_tumbling_number(i, a):
        res = 0
        if i+1 < len(A):
            for b in A[i+1:]:
                if a > b:
                    res += 1    
        return res   

    res = 0
    for i in range(N):
        tumbling_number_A = calc_tumbling_number(i, A[i])
        tumbling_number_B = calc_tumbling_number(-1, A[i])

        # 先頭のAに対する転倒数
        res += tumbling_number_A * K
        res %= MOD
        # 先頭より後ろの転倒数
        res += tumbling_number_B * ((K*(K-1)) // 2)
        res %= MOD

    print(res)

if __name__ == '__main__':
    main()