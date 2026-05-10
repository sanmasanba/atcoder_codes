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
from typing import Generic, Iterable, Iterator, NamedTuple,\
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

class Scc(NamedTuple):
    sccs: List[List[int]]
    comp_id: List[int]
    dag: List[List[int]]

def scc(G: List[List[int]], N: int) -> Scc:
    """
    Kosaraju法で強連結成分分解を行い、縮約DAGも構築する。

    Args:
        G: 有向グラフ（隣接リスト）
        N: 頂点数（0-indexed）

    Returns:
        Scc:
            sccs: 各強連結成分の頂点リスト
            comp_id: 各頂点が属する成分番号
            dag: 成分を縮約したDAG（隣接リスト）
    """
    H = [[] for _ in range(N)]
    for u in range(N):
        for v in G[u]:
            H[v].append(u)

    Scc = namedtuple('Scc', ['sccs', 'comp_id', 'dag'])

    used = [False] * N
    I = []

    def dfs1(v: int):
        used[v] = True
        for nextv in G[v]:
            if not used[nextv]:
                dfs1(nextv)
        I.append(v)

    for i in range(N):
        if not used[i]:
            dfs1(i)

    used = [False] * N
    sccs = []
    comp_id = [-1] * N

    def dfs2(v: int, cid: int, connected_nodes: List[int]):
        used[v] = True
        connected_nodes.append(v)
        comp_id[v] = cid
        for nextv in H[v]:
            if not used[nextv]:
                dfs2(nextv, cid, connected_nodes)

    I.reverse()
    for i in I:
        if used[i]:
            continue
        connected_nodes = []
        cid = len(sccs)
        dfs2(i, cid, connected_nodes)
        sccs.append(connected_nodes)

    dag_sets = [set() for _ in range(len(sccs))]
    for u in range(N):
        for v in G[u]:
            u_id = comp_id[u]
            v_id = comp_id[v]
            if u_id != v_id:
                dag_sets[u_id].add(v_id)

    dag = [list(s) for s in dag_sets]
    return Scc(sccs, comp_id, dag)

# main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    
    G = [[] for _ in range(N)]
    for u, v in enumerate(A):
        G[u].append(v-1)

    sccs = scc(G, N)
    M = len(sccs.sccs)
    reachable = [-1] * M
    def dfs(u):
        if reachable[u] != -1:
            return reachable[u]
        res = len(sccs.sccs[u])
        for v in sccs.dag[u]:  
            res += dfs(v)
        reachable[u] = res
        return reachable[u]
    
    for u in range(M):
        if reachable[u] < 0:
            dfs(u)
    
    res = 0
    for i in range(M):
        res += reachable[i] * len(sccs.sccs[i])
    print(res)

if __name__ == '__main__':
    main()