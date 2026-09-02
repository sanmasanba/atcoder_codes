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

# functional graph の閉路上のノードは入次数0のノード削除でわかる

# main
def main():
    # intput
    N = int(input())
    A = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))

    # 入次数を数える
    in_e = [0]*N
    for b in A:
        in_e[b] += 1

    # 入次数 0 の要素を列挙
    stc = [i for i, e in enumerate(in_e) if e == 0]

    # 入次数 0 の頂点を連鎖的に消せば残りはループ上にある
    while stc:
        cur = stc.pop()
        if 0 < in_e[cur]:
            continue
        # cur を削除し、cur -> nxt なノードの次数を-1
        in_e[A[cur]] -= 1
        # もし入次数が 0 になったなら削除に追加
        if in_e[A[cur]] == 0:
            stc.append(A[cur])

    # 先頭から見て閉路に含まれる中で最小のものを列挙していく
    res = 0
    for s in range(N):
        if in_e[s] == 0:
            continue
        tmp = C[s]
        while in_e[s]:
            tmp = min(tmp, C[s])
            in_e[s] = 0
            s = A[s]
        res += tmp
    print(res)

if __name__ == '__main__':
    main()
