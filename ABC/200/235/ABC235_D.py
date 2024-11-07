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
    a, N = map(int, input().split(' '))
    
    num_set = [INF] * (10**6+1)
    num_set[1] = 0
    que = deque()
    que.append(1)
    while que:
        num = que.popleft()
        tmp = []
        tmp.append(num * a)
        if num >= 10 and num % 10:
            num = str(num)
            tmp.append(int(num[-1] + num[:-1]))
        for n in tmp:
            if n <= 10**6:
                if num_set[int(num)]+1 < num_set[n]:
                    num_set[n] = num_set[int(num)] + 1
                    que.append(n)
                    
    print(-1 if num_set[N] == INF else num_set[N])

if __name__ == '__main__':
    main()