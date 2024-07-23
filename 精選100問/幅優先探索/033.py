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
def bfs(MAP, seen, s, g):
    # dist:vからの距離, queue:探索キュー
    H = len(MAP)
    W = len(MAP[0])
    # 距離保存用
    dist = [[0 for j in range(W)] for i in range(H)] 
    queue = deque()
    # 初期地点を1とする
    dist[s[0]][s[1]] = 1
    queue.append(s)
    while queue:
        v = queue.popleft()
        for next_v in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            next_i = v[0] + next_v[0]
            next_j = v[1] + next_v[1]
            # 範囲外なら無視
            if not 0 <= next_i < H or not 0 <= next_j < W:
                continue
            # 探索済みか"#"なら無視
            if dist[next_i][next_j] != 0 or MAP[next_i][next_j] == "#":
                continue
            dist[next_i][next_j] = dist[v[0]][v[1]] + 1
            queue.append((next_i, next_j))
    return dist[-1][-1]

#main
def main():
    H, W = map(int, input().split(' '))
    MAP = [input() for _ in range(H)]
    tmp = ''
    for i in MAP:
        tmp += i
    seen = [[0 for j in range(W)] for i in range(H)]
    res = bfs(MAP, seen, (0, 0), (-1, -1))

    print(-1 if res == 0 else H*W - res - Counter(tmp)["#"])

if __name__ == '__main__':
    main()