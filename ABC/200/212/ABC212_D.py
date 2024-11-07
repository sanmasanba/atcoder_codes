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
    bag = []
    offset = 0
    for _ in range(Q):
        input_ = input()
        if input_.startswith('1'):
            _, x = map(int, input_.split())
            heappush(bag, x-offset)
        elif input_.startswith('2'):
            _, x = map(int, input_.split())
            offset += x
        else:
            ans = heappop(bag)
            ans += offset
            print(ans)

if __name__ == '__main__':
    main()