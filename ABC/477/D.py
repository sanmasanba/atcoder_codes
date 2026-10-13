# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, isqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    N, Q = map(int, input().split())

    qry = [['2', 'a']]
    state = [0] * N
    for _ in range(1, Q+1):
        query = list(input().split())
        qry.append(query)
        if query[0] == '1':
            state[int(query[1])-1] ^= 1
    
    res = [None] * N
    s = set(i for i in range(N) if state[i] == 0)

    for query in reversed(qry):
        if query[0] == '1':
            x = int(query[1]) - 1
            # 色が未定で置かれていたところは更新対象にしない
            if state[x] == 0 and res[x] is None:
                s.discard(x)
            # 色が未定で、置かれていなかったところは更新対象
            if state[x] == 1 and res[x] is None:
                s.add(x)
            state[x] ^= 1
        else:
            for i in s:
                res[i] = query[1]
            s = set()

    print(''.join(res))

if __name__ == '__main__':
    main()
