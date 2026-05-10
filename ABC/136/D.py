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
    S = list(input())
    N = len(S)

    loop_pos = []

    for i in range(N-1):
        if S[i] != S[i+1]:
            loop_pos.append((i, i+1))

    res = [0]*N
    for i, s in enumerate(S):
        if s == 'R':
            idx = bisect_left(loop_pos, i, key=lambda x: x[0])
            move_dist = loop_pos[idx][0]-i
            res[i+move_dist+move_dist%2] += 1
        if s == 'L':
            idx = bisect_left(loop_pos, i, key=lambda x: x[1])
            if len(loop_pos) <= idx:
                idx -= 1
            if S[loop_pos[idx][0]] == 'L':
                idx -= 1
            move_dist = i-loop_pos[idx][1]
            res[i-move_dist-move_dist%2] += 1
    print(res)

if __name__ == '__main__':
    main()