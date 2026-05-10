#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, accumulate

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    # roaps[i] := i番目のロープの[Rの結び先、Bの結び先]
    G = [[] for _ in range(N)]
    deg = [0] * N
    for _ in range(M):
        a, b, c, d = input().split(' ')
        a = int(a)-1; c = int(c)-1
        G[a].append(c)
        G[c].append(a)
        deg[a] += 1
        deg[c] += 1
    
    loop = 0
    non_loop = 0
    used = [False] * N
    for roap in range(N):
        if not used[roap]:
            que = deque([roap])
            used[roap] = True
            flg = True
            while que:
                q = que.popleft()
                if deg[q] != 2:
                    flg = False
                for v in G[q]:
                    if not used[v]:
                        que.append(v)
                        used[v] = True
            if flg:
                loop += 1
            else:
                non_loop += 1

    print(loop, non_loop)

if __name__ == '__main__':
    main()