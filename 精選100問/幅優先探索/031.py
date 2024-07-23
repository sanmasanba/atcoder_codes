#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# 奇数列
ODD_ROW = [[0, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
# 偶数列
EVEN_ROW = [[0, -1], [-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1]]

#BFS
def bfs(MAP, s, seen):
    # dist:vからの距離, queue:探索キュー
    queue = deque()
    queue.append(s)
    H, W = len(seen), len(seen[0])
    seen[0][0] = 1
    while queue:
        v = queue.popleft()
        next_pos = ODD_ROW if v[0]%2 else EVEN_ROW
        for add_h, add_w in next_pos:
            # 次の座標を探索
            next_i = v[0] + add_h
            next_j = v[1] + add_w
            # 範囲外なら無視
            if not 0 <= next_i < H or not 0 <= next_j < W:
                continue
            # もともと１の部分と、探索済みは無視
            if seen[next_i][next_j] != 0 or MAP[next_i][next_j]:
                continue
            # 探索済みにする
            seen[next_i][next_j] =  1
            queue.append((next_i, next_j))
    return seen

#main
def main():
    W, H = map(int, input().split(' '))
    MAP = [[0 for _ in range(W+2)]]
    for _ in range(H):
        MAP.append([0] + list(map(int, input().split(' '))) + [0])
    MAP.append([0 for _ in range(W+2)])
    
    seen = [[0 for j in range(W+2)] for i in range(H+2)]
    bfs(MAP, [0, 0], seen)
    for i in range(H+2):
        for j in range(W+2):
            if seen[i][j] == 0:
                MAP[i][j] = 1

    res = 0
    for i in range(H+2):
        for j in range(W+2):
            next_pos = ODD_ROW if i%2 else EVEN_ROW
            for add_h, add_w in next_pos:
                # 次の座標を探索
                next_i = i + add_h
                next_j = j + add_w
                # 範囲外なら無視
                if not 0 <= next_i < H+2 or not 0 <= next_j < W+2:
                    continue
                if MAP[i][j] ^ MAP[next_i][next_j]:
                    res += 1
    print(res//2)

if __name__ == '__main__':
    main()