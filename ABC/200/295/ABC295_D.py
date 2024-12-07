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
    S = list(map(int, list(input())))
    mp = defaultdict(int)
    cnt = [0]*10
    mp[tuple(cnt)] += 1

    # うれしい列の時、登場回数のパリティが一致する
    for s in S:
        cnt[s] += 1
        cnt[s] %= 2
        mp[tuple(cnt)] += 1
    
    # 登場回数の数の組み合わせの数の総和が答え
    res = 0
    for nx in mp.values():
        res += (nx * (nx-1)) // 2
    
    print(res)

if __name__ == '__main__':
    main()