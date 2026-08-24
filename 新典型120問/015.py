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

# 考察
# クエリに着目するとk <= 3までしかかんがえなくていい
# 頂点あたり最大の次数3である場合
# d=0 : 1
# d=1 : 3
# d=2 : 9
# d=3 : 27
# なので、全頂点につきすべてを考慮しても、たかだか40点しか保持しない
# -> 全部保持して累積和で行けそう

# main
def main():
    # intput
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    # 1) 事前に計算する
    # BFS
    def bfs(G, N, s):
        # dist:vからの距離, queue:探索キュー
        seen = set()
        queue = deque()
        ret = [set() for _ in range(4)]
        seen.add(s)
        queue.append((s, 0))
        ret[0].add(s + 1)
        while queue:
            v, dist = queue.popleft()
            if 3 <= dist:
                continue
            for next_v in G[v]:
                if next_v in seen:
                    continue
                seen.add(next_v)
                next_dist = dist + 1
                ret[next_dist].add(next_v + 1)
                queue.append((next_v, next_dist))
        return ret

    memo = []
    for s in range(N):
        tmp = bfs(G, N, s)
        cumsum = [0]
        for d in range(4):
            cumsum.append(cumsum[-1] + sum(tmp[d]))
        memo.append(cumsum)
    
    Q = int(input())
    for _ in range(Q):
        x, k = map(int, input().split())
        x -= 1
        print(memo[x][k+1])

if __name__ == '__main__':
    main()
