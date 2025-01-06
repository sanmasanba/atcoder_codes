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
    A = list(map(int, input().split()))
    S = list(input())

    def cumsum(target: str):
        cnt_0 = [0]*N
        cnt_1 = [0]*N
        cnt_2 = [0]*N
        for i, s in enumerate(S):
            if s == target:
                match A[i]:
                    case 0:
                        cnt_0[i] = 1
                    case 1:
                        cnt_1[i] = 1
                    case 2:
                        cnt_2[i] = 1
        cumsum_0 = [0] + list(accumulate(cnt_0))
        cumsum_1 = [0] + list(accumulate(cnt_1))
        cumsum_2 = [0] + list(accumulate(cnt_2))

        return cumsum_0, cumsum_1, cumsum_2

    def solve(aj:int , X_cnt: List[int]):
        res = [0]
        for i, s in enumerate(S):
            res.append(res[-1])
            if s == 'E' and A[i] == aj:
                res[-1] += X_cnt[-1]-X_cnt[i]
        return res 

    def mex(ai, aj, ak):
        tmp = sorted([ai, aj, ak])
        return min([i for i in range(4) if i not in tmp])

    # それぞれの出現数の累積和を求める
    X0, X1, X2 = cumsum('X')    

    # si,sk = "EX"となる組み合わせのうち、(aj, ak)の登場回数
    EX = {}
    for aj in range(3):
        for ak, x in enumerate([X0, X1, X2]):
            EX[(aj, ak)] = (solve(aj, x))

    # Si = 'M'なものだけ考える
    res = 0
    for i, s in enumerate(S):
        if s != 'M':
            continue
        ai = A[i]
        for k, ex in EX.items():
            aj, ak = k
            res += mex(ai, aj, ak)*(ex[-1]-ex[i])

    print(res)

if __name__ == '__main__':
    main()