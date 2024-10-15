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

visited = set()
def bfs(S, H, W, h, w):
    global visited
    current_visited= set()
    current_visited.add((h, w))
    if S[h][w] == '-':
        return 1
    visited.add((h, w))
    queue = deque()
    queue.append((h, w))
    while queue:
        h, w = queue.popleft()
        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_h = h+dh; next_w = w+dw
            next_v = (next_h, next_w)
            if not (0 <= next_h < H) or not (0 <= next_w < W):
                continue
            if next_v in current_visited or S[next_h][next_w] == '#':
                continue
            if S[next_h][next_w] == '.':
                visited.add(next_v)
            if S[next_h][next_w] == '.':
                queue.append(next_v)
            current_visited.add(next_v)
    return len(current_visited)

#main
def main():
    global visited
    H, W = map(int, input().split(' '))
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)

    for h in range(H):
        for w in range(W):
            if 0 < h and S[h-1][w] == '#' and S[h][w] != '#':
                S[h][w] = '-'
            if  h < H-1 and S[h+1][w] == '#' and S[h][w] != '#':
                S[h][w] = '-'
            if 0 < w and S[h][w-1] == '#' and S[h][w] != '#':
                S[h][w] = '-'
            if w < W-1 and S[h][w+1] == '#' and S[h][w] != '#':
                S[h][w] = '-'

    res = 1
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#' or (h, w) in visited:
                continue
            else:
                res = max(res, bfs(S, H, W, h, w))
    print(res)

if __name__ == '__main__':
    main()