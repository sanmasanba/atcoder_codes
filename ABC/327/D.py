#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
bipartile = True

#BFS
# i:目標ノード、x:目標ノードのbit
def bfs(G, i, x, X):
    global bipartile
    # 現在のノードを、0 か 1 に割り振る
    X[i] = x
    # 現在のノードからつながるノードに反転ビットを書き込みに行く
    for next_i in G[i]:
        # 未到達ノードなら書き込む
        if X[next_i] == -1:
            bfs(G, next_i, 1-x, X)
        # 到達済みなら判定
        elif X[i] == X[next_i]: 
            bipartile = False

#main
def main():
    N, M = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    A = map(lambda x: int(x)-1, input().split(' '))
    B = map(lambda x: int(x)-1, input().split(' '))
    for a, b in zip(A, B):
        G[a].append(b)
        G[b].append(a)

    # 二分グラフを考える(到達していないノードが-1)
    X = [-1 for _ in range(N)]
    # 判定
    for i in range(N):
        if X[i] == -1:
            bfs(G, i, 0, X)

    print('Yes' if bipartile else 'No')
    
if __name__ == '__main__':
    main()