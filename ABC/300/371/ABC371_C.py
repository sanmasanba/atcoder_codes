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
    N = int(input())
    Mg = int(input())
    G = set()
    for _ in range(Mg):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        G.add((a, b))
        G.add((b, a))
    Mh = int(input())
    H = set()
    for _ in range(Mh):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        H.add((a, b))
        H.add((b, a))

    A = [[0 for _ in range(N)] for _ in range(N)]
    # 逆向きのコストも追加
    for i in range(N-1):
        tmp = list(map(int, input().split(' ')))
        for j, a in enumerate(tmp, start=i+1):
            A[i][j], A[j][i] = a, a

    # Hの頂点をGに対応させる表を順列全探索
    # Hのi番目がGのP[i]番目に対応する
    P = [i for i in range(N)]
    ans = INF

    for perm in permutations(P):
        tmp_cnt = 0
        for i in range(N):
            for j in range(i):
                # 1:Hに(i, j)が含まれて、Gに(perm[i], perm[j])が含まれない
                # 2:Hに(i, j)が含まれず、Gに(perm[i], perm[j])が含まれる
                # のどちらかなら辺に手を加える必要がある
                if ((i, j) in H) != ((perm[i], perm[j]) in G):
                    tmp_cnt += A[i][j]
        ans = min(ans, tmp_cnt)
    print(ans)

if __name__ == '__main__':
    main()