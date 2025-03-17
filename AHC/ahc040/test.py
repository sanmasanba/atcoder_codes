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
import random
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

def main():
    N, T, sigma = map(int, input().split(' '))
    W, H = zip(*[list(map(int, input().split(' '))) for _ in range(N)])
    target_W = sqrt(sum(w*h for w, h in zip(W, H)))
    rnd = random.Random(42)

    for _ in range(T):
        res = []
        crr_w = 0
        crr_target = -1
        flg = 0
        for i, wh in enumerate(zip(H, W)):
            w, _ = wh
            if crr_w + w <= target_W:
                res.append((i, 
                            rnd.randint(0, 1), 
                            'L' if flg else 'U', 
                            -1 if flg else i-1))
                crr_w += w
            else:
                res.append((i, 
                            rnd.randint(0, 1), 
                            'U', 
                            -1))
                crr_w = w
                flg = 0

        print(len(res), flush=True)
        for r in res:
            print(*r, flush=True)
        __, _ = map(int, input().split(' '))
        
        
if __name__ == '__main__':
    main()