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

#main
def main():
    # intput
    N, M = map(int, input().split())
    DAG = {i:[] for i in range(N)}
    for _ in range(M):
        x, y = map(lambda x: int(x)-1, input().split())
        DAG[x].append(y)

    
    # topo_sort
    topo_sort = []
    ind = [0] * N
    # 入次数を求める
    for v in range(N):
        for nv in DAG[v]:
            ind[nv] += 1
    que = []
    # 入次数が0のノードがスタート
    for v in range(N):
        if ind[v] == 0:
            que.append(v)
    
    while que:
        # 1 < len(que)のとき、トポロジカル順序が一意でない
        # -> 並び順に複数の候補が存在するため、数列Aは一意に定まらない
        if 1 < len(que):
            print('No')
            return
        
        v = heappop(que)
        topo_sort.append(v+1)
        for nv in DAG[v]:
            ind[nv] -= 1
            if ind[nv] == 0:
                heappush(que, nv)
    if len(topo_sort) != N:
        print('No')
        return
    
    res = [0]*N
    for i, d in enumerate(topo_sort): res[d-1] = i+1
    print('Yes')
    print(*res)

if __name__ == '__main__':
    main()