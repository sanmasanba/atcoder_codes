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
    N, M, Q = map(int, input().split(' '))
    W, V = zip(*[list(map(int, input().split(' '))) for _ in range(N)])
    X = [(x, i) for i, x in enumerate(list(map(int, input().split(' '))))]
    X.sort()

    # 小さい箱から、価値が最大化するように詰める
    for _ in range(Q):
        L, R = map(lambda x: int(x)-1, input().split(' '))

        used = [False]*N
        res = 0
        for box_num in range(M):
            if L <= X[box_num][1] <= R:
                continue
            max_v = -1
            max_idx = -1
            for idx in range(N):
                if not used[idx] and W[idx] <= X[box_num][0] and max_v < V[idx]:
                    max_v = V[idx]
                    max_idx = idx
            
            if -1 < max_idx:
                used[max_idx] = True
                res += max_v

        print(res)

if __name__ == '__main__':
    main()