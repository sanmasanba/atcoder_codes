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
MOD = 998244353

#main
def main():
    # intput
    H, W = map(int, input().split(' '))
    S = [list(input()) for _ in range(H)]

    # ある２＊２マスで考えると、左上から右下に向かうためには
    # 右上と左下が同じ色である必要がある
    # -> h + w が等しいマス同士では、色が等しい必要がある
    # -> '.'なら、'R'でも'B'でもよい　-> 全てのマスで2倍の通り数になる
    # -> 'R'も'B'もあるとき、矛盾が生じる -> どの移動でも等しい移動ができない
    res = 1
    HW = H+W-1
    for hw in range(HW):
        mp = [0]*3
        for h in range(H):
            if 0 <= hw-h < W:
                match S[h][hw-h]:
                    case '.':
                        mp[0] += 1
                    case 'R':
                        mp[1] += 1
                    case 'B':
                        mp[2] += 1
        if mp[1] == 0 and mp[2] == 0:
            res *= 2
        elif 0 < mp[1] and 0 < mp[2]:
            res *= 0
        res %= MOD
    
    print(res)

if __name__ == '__main__':
    main()