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
    Q = int(input())

    snakes = [0]
    top = 0
    res = []
    for _ in range(Q):
        S = input()
        match S[0]:
            case '1':
                _, x = S.split()
                snakes.append(snakes[-1] + int(x))
            case '2':
                top += 1
            case '3':
                _, x = S.split()
                res.append(snakes[top+int(x)-1] - snakes[top])
    
    print(*res, sep='\n')

if __name__ == '__main__':
    main()