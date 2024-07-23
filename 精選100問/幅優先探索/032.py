#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#BFS
def bfs(walls_set, dist, s):
    # dist:vからの距離, queue:探索キュー
    queue = deque()
    H = len(dist)
    W = len(dist[0])
    dist[0][0] = 1
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next_v in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            next_i = v[0] + next_v[0]
            next_j = v[1] + next_v[1]
            # マップの外なら無視
            if not 0 <= next_i < H or not 0 <= next_j < W:
                continue
            # 探索済みか、壁があるときに無視
            if  dist[next_i][next_j] != -1 or (next_i, next_j) in walls_set[v[0]][v[1]]:
                continue
            dist[next_i][next_j] = dist[v[0]][v[1]] + 1
            queue.append((next_i, next_j))
    return dist

#main
def main():
    res = []
    while 1:
        W, H = map(int, input().split(' '))
        if W == 0 and H == 0:
            break
        # 壁を辞書型で管理
        walls_set = [[set() for j in range(W)] for i in range(H)]
        for h in range(2*H-1):
            line = input().strip()
            walls = list(map(int, line.split()))
            # 偶数列
            if h%2 == 0:
                # 壁があるときに双方向リストと同様に保存
                for i, wall in enumerate(walls):
                    if wall:
                        walls_set[h//2][i].add((h//2, i+1))
                        walls_set[h//2][i+1].add((h//2, i))
            # 奇数列
            else:
                # 壁があるときに双方向リストと同様に保存
                for i, wall in enumerate(walls):
                    if wall:
                        walls_set[h//2][i].add((h//2+1, i))
                        walls_set[h//2+1][i].add((h//2, i))

        dist = [[-1 for j in range(W)] for i in range(H)]
        # 幅優先探索
        bfs(walls_set, dist, (0, 0))  
        # 一番端がゴール 
        res.append(dist[-1][-1]) 
    for i in res:
        # -1のとき、そのマップはゴールにたどり着けない
        print(0 if i == -1 else i)

if __name__ == '__main__':
    main()