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


def suffix_array(S: str) -> list[int]:
    """ダブリングを使った O(Nlog^2N) suffix array 構築

    Args:
        S (str): 構築対象
    """
    n = len(S)

    if n == 0:
        return []

    ret = list(range(n))
    rank = [ord(S[i]) - 97 for i in range(n)]
    tmp = [0] * n

    k = 1
    while k < n:

        fn = lambda x: (rank[x], rank[x+k] if x+k < n else -1)

        ret.sort(key=fn)

        tmp[ret[0]] = 0
        for i in range(1, n):
            tmp[ret[i]] = tmp[ret[i-1]] + (
                1 if fn(ret[i-1]) < fn(ret[i]) else 0
            )
                

        rank, tmp = tmp, rank
        k *= 2

    return ret


# main
def main():
    # intput
    print(suffix_array("banana"))

if __name__ == '__main__':
    main()
