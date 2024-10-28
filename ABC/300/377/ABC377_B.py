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
    Ss = []
    for _ in range(8):
        S  = input()
        if '#' in S:
            S = S.replace('.', '$')
        Ss.append(S)
    tmp = []
    for s in zip(*Ss): tmp.append(list(s))
    res = 0
    for S in tmp:
        if '#' not in S:
            for s in S:    
                res += 1 if s == '.' else 0
    print(res)

if __name__ == '__main__':
    main()