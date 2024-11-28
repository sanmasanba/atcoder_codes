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
from string import ascii_lowercase

T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # intput
    N = int(input())
    S = [input() for _ in range(N)]
    res = [0] * N

    def dfs(pref, idx):
        group = [[] for _ in range(26)]
        # それぞれのk文字目を見て分類する
        for i in idx:
            if pref < len(S[i]):
                group[ord(S[i][pref]) - ord('a')].append(i)
        # 一旦記録
        for i in idx:
            res[i] = pref
        # 分類後、k文字目が同じものが2つ以上あるなら再帰
        for g in group:
            if 2 <= len(g):
                dfs(pref + 1, g)
    
    all_idx = list(range(N))
    dfs(0, all_idx)
    for x in res:
        print(x)

if __name__ == '__main__':
    main()