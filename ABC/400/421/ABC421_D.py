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

def input_actions(n):
    tmp = []
    for _ in range(n):
        c, cnt = input().split()
        if c == 'U':
            tmp.append((-1, 0, int(cnt)))
        elif c == 'D':
            tmp.append((1, 0, int(cnt)))
        elif c == 'L':
            tmp.append((0, -1, int(cnt)))
        else:
            tmp.append((0, 1, int(cnt)))
    return tmp

# main
def main():
    # intput
    x1, y1, x2, y2 = map(int, input().split())
    _, N, L = map(int, input().split())

    S = input_actions(N)
    T = input_actions(L)

    def check(gx, gy, vx, vy):
        # x方向に変化がなく、y軸方向にのみ移動
        if vx == 0 and gx == 0 and vy != 0 and gy % vy == 0:
            time = -gy // vy
            return 1 <= time <= step
        # y方向に変化がなく、x軸方向にのみ移動
        elif vy == 0 and gy == 0 and vx != 0 and gx % vx == 0:
            time = -gx // vx
            return 1 <= time <= step
        # どちらも変化するとき、重複が発生するかを判定
        elif vx != 0 and vy != 0 and gx % vx == 0 and gy % vy == 0:
            tx = -gx // vx
            ty = -gy // vy
            return 1 <= tx <= step and tx == ty
        return False

    i, j = 0, 0
    si = S[0][2]
    tj = T[0][2]
    ans = 0

    # 両方の移動が終わるまで
    while i < N and j < L:
        # 移動方向と最小移動量
        dx1, dy1, _ = S[i]
        dx2, dy2, _ = T[j]
        step = min(si, tj)
        
        # 相対位置ベクトルと相対方向ベクトル
        gx, gy = x1 - x2, y1 - y2
        vx, vy = dx1 - dx2, dy1 - dy2
        
        # 相対位置が変化しいとき(方向ベクトルが等しい)
        if vx == 0 and vy == 0:
            # 初期値点が等しいとき
            if gx == 0 and gy == 0:
                ans += step
        # 相対位置が変化するとき(方向ベクトルが等しくない)
        else:
            ans += 1 if check(gx, gy, vx, vy) else 0
        
        # 位置と移動量の更新
        x1 += dx1 * step
        y1 += dy1 * step
        x2 += dx2 * step
        y2 += dy2 * step
        si -= step
        tj -= step
        
        # 移動量が0の場合に次のステップに移行
        if si == 0:
            i += 1
            if i < N: si = S[i][2]

        if tj == 0:
            j += 1
            if j < L: tj = T[j][2]

    print(ans)

if __name__ == '__main__':
    main()