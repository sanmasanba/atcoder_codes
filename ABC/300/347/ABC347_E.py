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
    N, Q = map(int, input().split(' '))
    x = list(map(lambda x: int(x)-1, input().split(' ')))
    
    S = set()
    SUM = [0]
    seen = [[] for _ in range(N)]
    for i, xi in enumerate(x):
        # それぞれの数字の登場回を記録
        seen[xi].append(i)
        if xi in S: S.discard(xi)
        else: S.add(xi)
        # 累積和を管理
        SUM.append(SUM[-1] + len(S))

    A = [0]*N
    for i in range(N):
        # もし登場回数が奇数なら偶数回にそろえる
        if len(seen[i])%2:
            seen[i].append(Q)
        
        # 偶数回の累積和 - 奇数回の累積和で増加分が計算できる
        for j in range(len(seen[i])//2):
            A[i] += SUM[seen[i][2*j+1]] - SUM[seen[i][2*j]]

    print(*A)    

if __name__ == '__main__':
    main()