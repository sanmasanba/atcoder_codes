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
    P = list(map(int, input().split(' ')))
    # 自身に対応する皿が来るまでの距離を求める
    dists = [0 for i in range(N)]
    for i, p in enumerate(P):
        if p <= i:
            dists[i-p] += 1 
        else:
            dists[(i-p+N)%N] += 1 

    # 移動距離を基準に全探索
    res = 0
    for i in range(N):
        res = max(res, dists[(i-1)%N]+dists[i%N]+dists[(i+1)%N])
    print(res)

if __name__ == '__main__':
    main()