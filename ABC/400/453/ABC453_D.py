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

move2d = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# main
def main():
    # intput
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    
    for r in range(H):
        for c in range(W):
            if S[r][c] == 'S': s = (r, c)
            if S[r][c] == 'G': g = (r, c)
    
    seen = [[[None for _ in range(W)] for _ in range(H)] for _ in range(4)]
    queue = deque()
    queue.append((s, -1))

    while queue:
        ((pr, pc), pre_dir) = queue.popleft()
        if (pr, pc) == g:
            break
        if S[pr][pc] == 'o':
            (dr, dc) = d[pre_dir]
            nr = pr + dr
            nc = pc + dc
            if ((0 <= nr < H and 0 <= nc < W) 
                and seen[pre_dir][nr][nc] is None
                and S[nr][nc] != '#'):
                seen[pre_dir][nr][nc] = (pre_dir, pr, pc)
                queue.append(((nr, nc), pre_dir))
        else:
            for nxt_dir, (dr, dc) in enumerate(d):
                nr = pr + dr
                nc = pc + dc
                # 範囲外あるいはおなじ方法で到達済み
                if not (0 <= nr < H and 0 <= nc < W) or seen[nxt_dir][nr][nc] is not None:
                    continue
                # 現在xの場合は、同じ方向は無理
                if S[pr][pc] == 'x' and nxt_dir == pre_dir:
                    continue
                # #は移動できない
                if S[nr][nc] in ('S', '#'):
                    continue
                seen[nxt_dir][nr][nc] = (pre_dir, pr, pc)
                queue.append(((nr, nc), nxt_dir))
    
    res = []
    for dir in range(4):
        if seen[dir][g[0]][g[1]]: 
            print("Yes")
            res.append(dir)
            pre_dir, pr, pc = seen[dir][g[0]][g[1]]
            while (pr, pc) != s:
                res.append(pre_dir)
                if seen[pre_dir][pr][pc] is None:
                    break
                pre_dir, pr, pc = seen[pre_dir][pr][pc]
            print(''.join(reversed(list(map(lambda x: move2d[x], res)))))
            return
    print("No")

if __name__ == '__main__':
    main()