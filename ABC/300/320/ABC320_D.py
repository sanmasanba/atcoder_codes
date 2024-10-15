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
    # input
    N, M = map(int, input().split(' '))
    G = defaultdict(list)
    for _ in range(M):
        s, g, *weight = map(int, input().split(' '))
        G[s-1].append((g-1, weight))
        G[g-1].append((s-1, list(map(lambda x: -x, weight))))    

    res = [-1 for _ in range(N)]
    res[0] = (0, 0)
    #BFS
    queue = deque()
    queue.append(0)
    while queue:
        v = queue.popleft()
        for next_v, d in G[v]:
            if res[next_v] != -1:
                continue
            x = res[v][0] + d[0]
            y = res[v][1] + d[1]
            res[next_v] = (x, y)
            queue.append(next_v)    

    # output
    for r in res:
        if r == -1:
            print('undecidable')
        else:
            print(*r)

if __name__ == '__main__':
    main()