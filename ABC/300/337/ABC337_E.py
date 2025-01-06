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
    
    M = 1
    while 2**M < N:
        M += 1
    print(M)
    
    juices = []
    for i in range(M): 
        cnt = 2**i
        res = ''
        while len(res) < N:
            res = res + cnt*"0"
            res = res + cnt*"1"
        juices.append(res[:N])
        res = [j for j, c in enumerate(res[:N], start=1) if c == '1']
        print(len(res), *res, flush=True)
    
    S = input()
    res = 0
    for i, c in enumerate(S):
        if c == '1':
            res |= (1 << i)
    print(res+1)

    

if __name__ == '__main__':
    main()