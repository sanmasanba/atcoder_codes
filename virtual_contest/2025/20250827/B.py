# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
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
    N = int(input())
    res = 0
    memo = {"toA":0, "BtoA":0, "Bto":0}
    for _ in range(N):
        S = list(input().strip())
        for i in range(len(S)-2):
            if S[i] == 'A' and S[i+1] == 'B':
                res += 1
        if S[0] == 'B' and S[-1] == 'A':
            memo['BtoA'] += 1
        elif S[0] != 'B' and S[-1] == 'A':
            memo['toA'] += 1
        elif S[0] == 'B' and S[-1] != 'A':
            memo['Bto'] += 1
    # BtoAとBtoAの連結
    if 0 < memo['BtoA']:
        res += memo['BtoA'] - 1
        memo['BtoA'] = 1
    # BtoAの残りを消費
    if 0 < memo['BtoA']:
        if 0 < memo['Bto'] and 0 < memo['toA']:
            res += 2
            memo = {k:v-1 for k, v in memo.items()}
        elif 0 < memo['Bto']:
            res += 1
            memo['Bto'] -= 1
            memo['BtoA'] = 0
        elif 0 < memo['toA']:
            res += 1
            memo['toA'] -= 1
            memo['BtoA'] = 0
    # BtoとtoAのセットを消費
    res += min(memo['toA'], memo['Bto'])

    print(res)

if __name__ == '__main__':
    main()