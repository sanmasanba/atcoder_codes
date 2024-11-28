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
    N, K = map(int, input().split(' '))
    S = input()
    T = []
    tmp_cnt = 0
    tmp_pos = INF
    for i in range(N):
        s = S[i]
        if s == '1':
            tmp_cnt += 1
            tmp_pos = min(tmp_pos, i)
        elif 0 < tmp_cnt:
            T.append((tmp_cnt, tmp_pos))
            tmp_cnt = 0
            tmp_pos = INF
    if 0 < tmp_cnt:
            T.append((tmp_cnt, tmp_pos))
            tmp_cnt = 0
            tmp_pos = INF

    precnt, prepos = T[K-2]
    cnt, pos = T[K-1]
    tmpa = S[:prepos]
    tmpc = S[pos+cnt:]
    tmpb = S[prepos:pos]
    print(tmpa + '1'*cnt + tmpb + tmpc)        

if __name__ == '__main__':
    main()