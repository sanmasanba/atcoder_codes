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
    
    res = []
    que = deque([[a] for a in range(1, M+1-10*(N-1))])
    while que:
        curr = que.popleft()
        a = curr[-1] + 10
        while a < M+1-10*(N-len(curr)-1):
            if len(curr) < N-1:
                tmp = curr[:]
                tmp.append(a)
                que.append(tmp)
            else:
                res.append([*curr, a])
            a += 1
    
    print(len(res))
    for r in res:
        print(*r)

if __name__ == '__main__':
    main()