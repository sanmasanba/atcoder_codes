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

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    # DFS
    seen = set()
    last = [-1] * N
    stc = []
    def dfs(cur, d):
        seen.add(cur)
        stc.append(cur)
        last[cur] = d
        for nxt in G[cur]:
            # 到達済みで
            if nxt in seen:
                # 距離が2以上で偶数なら終わり
                # 元のノードに戻るので-1されてる
                dist = d+1 - last[nxt]
                if 3 <= dist and dist%2 == 1:
                    stc.append(nxt)
                    return True
                # そうでないなら単に戻る
                else:
                    continue
            if dfs(nxt, d+1):
                return True
        seen.discard(cur)
        stc.pop()
        last[cur] = -1
        return False
    
    dfs(0, 0)
    if not stc:
        print(-1)
        return
    else:
        res = []
        seen = set()
        for a in stc[::-1]:
            a += 1
            if a in seen:
                print(len(res))
                print(*res)
                return
            seen.add(a)
            res.append(a)
    print(len(res))
    print(*res)

# main
def main():
    # intput
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
