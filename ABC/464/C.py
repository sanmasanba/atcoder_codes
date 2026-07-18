# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
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
    N, M = map(int, input().split())
    kind = set()
    cnt = [0]*(N+1)
    ADB = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        ADB.append(tmp)
        kind.add(tmp[0])
        cnt[tmp[0]] += 1
    ADB = deque(sorted(ADB, key=lambda x: x[1]))

    for m in range(1, M+1):
        while ADB and ADB[0][1] <= m:
            a, _, b = ADB[0]
            cnt[a] -= 1
            cnt[b] += 1
            if cnt[a] <= 0: kind.remove(a)
            kind.add(b)
            ADB.popleft()
        print(len(kind))

if __name__ == '__main__':
    main()