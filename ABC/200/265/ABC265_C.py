#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    H, W = map(int, input().split(' '))
    MAP = [[0]*(W+2)]
    for _ in range(H):
        MAP.append([0] + list(input()) + [0])
    MAP.append([0]*(W+2))
    move = {'U':[-1, 0], 'D':[1, 0], 'L':[0, -1], 'R':[0, 1]}

    pos = [1, 1]
    while 1:
        next_move = move[MAP[pos[0]][pos[1]]]
        MAP[pos[0]][pos[1]] = 1
        pos = [pos[0]+next_move[0], pos[1]+next_move[1]]
        # 範囲外なら終わり
        if MAP[pos[0]][pos[1]] == 0:
            pos = [min(H, max(pos[0], 1)), min(W, max(pos[1], 1))]
            break
        # 一度来たとこなら終わり
        if MAP[pos[0]][pos[1]] == 1:
            pos = [-1]
            break

    print(*pos)

if __name__ == '__main__':
    main()