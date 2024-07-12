#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    A = list(map(int, ("0 " + input()).split(' ')))

    #開始地点
    pos = 1
    #N回移動することで必ず、いずれかの閉路に入った状態になる
    for _ in range(N):
        pos = A[pos]

    #閉路のどこかからスタート
    B = [pos]
    while B[0] != A[pos]:
        #次の頂点に移動
        pos = A[pos]
        #経路の追加
        B.append(pos)

    print(len(B))
    print(*B)

if __name__ == '__main__':
    main()