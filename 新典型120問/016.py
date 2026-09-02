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
# 有向グラフにしてみる
# 8
# 7 3 5 5 8 4 1 2
# 36 49 73 38 30 85 27 45
#
# 上記の入力例を有向グラフとしてみてみると
# 非巡回 : {4, 6}
# 巡回 : {2, 3, 5, 8}, {1, 7}
# に分解できる
# ->巡回部分はその中で最小を選ぶ
# 　非巡回部分は逆順にすれば0
# 制約的に巡回を内包した巡回は発生しない(出辺に1なので)

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
    A = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    
    G = [[] for _ in range(N)]
    for a, b in enumerate(A):
        G[a].append(b)

    # scc を列挙する
    ret = scc(G, N)
    
    # 連結成分内で最小となるものを選んでいく
    res = 0
    for g in ret.sccs:
        if len(g) == 1:
            continue
        tmp = C[g[0]]
        for n in g[1:]:
            tmp = min(tmp, C[n])
        res += tmp
    print(res)

if __name__ == '__main__':
    main()
