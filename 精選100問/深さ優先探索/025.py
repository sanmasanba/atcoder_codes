#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')
seen = set()

# DFS
def dfs(G, v):
    # 頂点vを探索済みにする
    global seen
    seen.add(v)

    # 探索
    for next_v in G[v]:
        # 探索済みならスルー
        if next_v in seen:
            continue
        dfs(G, next_v)

#main
def main():
    global seen
    maps = deque()
    cnt = 0
    res = deque()
    # input 
    while 1:
        w, h = map(int, input().split(' '))
        if h == 0 and w == 0: break
        MAP = [list(map(int, input().split(' '))) for _ in range(h)]
        G = [[] for _ in range(h*w)]
        for i in range(h*w):
            H = i//w
            W = i%w
            for j, k in product([-1, 0, 1], repeat=2):
                try:
                    if j == 0 and k == 0:
                        pass
                    else:
                        if MAP[H][W] == 1 and MAP[H+j][W+k] == 1 and H+j >= 0 and W+k >= 0:
                            G[i].append(w*(H+j) + W+k)
                            G[w*(H+j) + W+k].append(i)
                except:
                    pass

        # 探索
        seen = set()
        ans = 0
        # 探索していない点からのグラフを調べ上げる
        for i in range(len(G)):
            # 探索してなくても海なら無視する
            if i not in seen and MAP[i//w][i%w] == 1:
                dfs(G, i)
                ans += 1
        res.append(ans)
    while res:
        tmp = res.popleft()
        print(tmp)

if __name__ == '__main__':
    main()