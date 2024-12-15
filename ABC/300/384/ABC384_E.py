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
    H, W, X = map(int, input().split(' '))
    P, Q = map(lambda x: int(x)-1, input().split(' '))
    S = [list(map(int, input().split(' '))) for _ in range(H)]
    used = [[0]*W for _ in range(H)]

    strength = S[P][Q]
    used[P][Q] = 1
    heap = []
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dp, dq in d:
        np, nq = P+dp, Q+dq
        if not (0 <= np < H and 0 <= nq < W):
            continue
        heappush(heap, (S[np][nq], (np, nq)))
    
    while heap and heap[0][0] < strength/X:
        s = heappop(heap)
        st, pos = s
        if used[pos[0]][pos[1]]:
            continue
        strength += st
        used[pos[0]][pos[1]] = 1
        for dp, dq in d:
            np, nq = pos[0]+dp, pos[1]+dq
            if not (0 <= np < H and 0 <= nq < W):
                continue
            if not used[np][nq]:
                heappush(heap, (S[np][nq], (np, nq)))

    print(strength)

if __name__ == '__main__':
    main()