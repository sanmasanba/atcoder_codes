#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
c2i = {c:i for i, c  in enumerate("snuke")}
i2c = {i:c for i, c  in enumerate("snuke")}
#BFS
def bfs(S:list, dist:list, s:list, g:list):
    res = False
    queue = deque([(0, 0, 0)])
    while queue:
        v = queue.pop()
        dist[v[0]][v[1]] = v[2]
        for dh, dw in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nexth, nextw = v[0]+dh, v[1]+dw
            # 次の座標が範囲外
            if not 0 <= nexth <= g[0] or not 0 <= nextw <= g[1]:
                continue
            # 次の座標が探索済
            if dist[nexth][nextw] != -1:
                continue
            if S[nexth][nextw] == i2c[(v[2]+1)%5]:
                if [nexth, nextw] == g:
                    res = True
                    break
                queue.append((nexth, nextw, (v[2]+1)%5))
    return res

#main
def main():
    H, W = map(lambda x: int(x)-1, input().split(' '))
    S = [list(input()) for _ in range(H+1)]
    if S[0][0] != 's':
        print("No")
    else:
        print("Yes" if bfs(S, [[-1]*(W+1) for _ in range(H+1)], [0, 0], [H, W]) else "No")

if __name__ == '__main__':
    main()