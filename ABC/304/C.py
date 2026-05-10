#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# DFS
seen = set()
infection = set()
def dfs(X, Y, N, D, v):
    # 頂点vを探索済みにする
    seen.add(v)
    infection.add(v)
    # 探索
    for next_v in range(N):
        # 探索済みか、感染済みならスルー
        if next_v in seen or next_v in infection:
            continue
        # 条件外ならスルー
        if D**2 < (X[v]-X[next_v])**2+(Y[v]-Y[next_v])**2:
            continue
        dfs(X, Y, N, D, next_v)
    seen.remove(v)

#main
def main():
    N, D = map(int, input().split(' '))
    X, Y = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        X.append(a)
        Y.append(b)
    dfs(X, Y, N, D, 0)
    for i in range(N):
        print('Yes' if i in infection else 'No')

if __name__ == '__main__':
    main()