#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

NEXT_way = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

sys.setrecursionlimit(10**6)
INF = float('inf')
def bfs(MAP, check_map, h, w):
    check_map[h][w] = 1
    stack = [(h, w)]
    while stack:
        v = stack.pop()
        # 探索済みにする
        check_map[v[0]][v[1]] = 1
        for next_h, next_w in NEXT_way:
            # 未探索なセンサーなら
            if check_map[v[0]+next_h][v[1]+next_w] == 0 and MAP[v[0]+next_h][v[1]+next_w] == '#':
                # stackに追加
                stack.append((v[0]+next_h, v[1]+next_w))

#main
def main():
    H, W = map(int, input().split(' '))
    MAP = [['.' for _ in range(W+2)]]
    for _ in range(H):
        MAP.append(list('.' + input() + '.'))
    MAP.append(['.' for _ in range(W+2)])
    check_map = [[0 for j in range(W+2)] for i in range(H+2)]

    res = 0
    for h in range(1, H+1):
        for w in range(1, W+1):
            if check_map[h][w] == 0 and MAP[h][w] == '#':
                res += 1
                bfs(MAP, check_map, h, w)
    print(res)

if __name__ == '__main__':
    main()