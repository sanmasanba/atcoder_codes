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
    # input
    N, M = map(int, input().split(' '))
    D = [1 for i in range(M+1)]
    # それぞれのRについて、[l, r]なる閉区間があるとき
    # [l, r]が満たすなら、より狭い[l+1, r]も条件を満たす
    # -> rを固定すれば、あるRに対して最大Lに1加えたものからが条件を満たす閉区間
    for _ in range(N):
        l, r = map(int, input().split(' '))
        D[r] = max(D[r], l+1)
    # あるrについて、rがどの区間の終端でもないとき
    # r-1の左端がrの左端になる
    for r in range(1, M+1):
        D[r] = max(D[r], D[r-1])
    res = 0
    for r in range(1, M+1):
        res += r - D[r] + 1

    print(res)

if __name__ == '__main__':
    main()
