#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

def search(G, visited, res):
    visited[res] = 1
    tofloor = res
    for i in G[res]:
        if visited[i] == 1:
            continue
        else:
            tofloor = max([tofloor, search(G, visited, i)])
    return tofloor

#main
def main():
    N = int(input())
    G = {}
    visited = {}
    #双方向グラフ
    for _ in range(N):
        a, b = map(int, input().split(' '))
        if a not in G:
            G[a] = [b]
        else:
            G[a].append(b)
        if b not in G:
            G[b] = [a]
        else:
            G[b].append(a)
        if a not in visited:
            visited[a] = 0
        if b not in visited:
            visited[b] = 0

    res = 1
    if res in G:
        res = search(G, visited, res)

    print(res)

if __name__ == '__main__':
    main()