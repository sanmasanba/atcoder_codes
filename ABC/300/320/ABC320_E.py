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
    N, M = map(int, input().split(' '))
    events = {}
    Ts = []
    peoples = [i for i in range(N)]
    for _ in range(M):
        T, W, S = map(int, input().split(' '))
        heappush(Ts, T)
        events[T] = {'W':W, 'S': S, 'N':[]}
    
    res = [0] * N
    while Ts:
        t = heappop(Ts)
        w, s, n = events[t].values()
        for p in n:
            heappush(peoples, p)
        if w is not None and peoples:
            p = heappop(peoples)
            res[p] += w
            if t+s not in events:
                events[t+s] = {'W':None, 'S': None, 'N':[]}
                heappush(Ts, t+s)
            events[t+s]['N'].append(p)
            
    print(*res, sep='\n')

if __name__ == '__main__':
    main()