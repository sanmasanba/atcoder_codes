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
    N, K = map(int, input().split())
    S = list(input().strip())
    
    rlc = []
    cnt, v = 1, S[0]
    for s in S[1:]:
        if v != s:
            rlc.append((v, cnt))
            v, cnt = s, 1
        else:
            cnt += 1
    rlc.append((v, cnt))

    idx = -1
    cnt = 0
    for i, (s, _) in enumerate(rlc):
        cnt += s == '1'
        if cnt == K:
            idx = i
            break
    
    print(''.join([s*v for (s, v) in rlc[:idx-1]])
          + rlc[idx][0]*rlc[idx][1]
          + rlc[idx-1][0]*rlc[idx-1][1]
          + ''.join([s*v for (s, v) in rlc[idx+1:]])
          )

if __name__ == '__main__':
    main()