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
    A = list(map(int, input().split(' ')))
    
    rle = []
    t = None
    cnt = 0
    for s in A:
        if t is None:
            t = s
            cnt += 1
            continue
        if t != s:
            if cnt <= 2:
                rle.append((t, cnt))
            else:
                rle.append((t, 2))
                rle.append((t, 2))
            t = s
            cnt = 1
        else:
            cnt += 1
    if cnt <= 2:
        rle.append((t, cnt))
    else:
        rle.append((t, 2))
        rle.append((t, 2))

    res = 0
    r = 0
    seen = set()
    for l in range(len(rle)):
        while r < len(rle) and rle[r][0] not in seen and 2 == rle[r][1]:
            seen.add(rle[r][0])
            r += 1

        res = max(res, (r-l)*2)
        if l == r:
            r += 1
        seen.discard(rle[l][0])
    
    print(res)

if __name__ == '__main__':
    main()