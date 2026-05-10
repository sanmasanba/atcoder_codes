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
    s2sc = {}
    sc2s = []
    # オリジナルを覚える連想配列と点数を覚える配列を別に準備
    for i in range(N):
        tmp = input().split(' ')
        s, x = tmp[0], int(tmp[1])
        if s not in s2sc:
            s2sc[s] = i+1
            sc2s.append([x, i+1, s])
    # 点数順にソート
    sc2s.sort(key=lambda x: (x[0], -x[1]))
    best_s = sc2s[-1][2]
    
    print(s2sc[best_s])

if __name__ == '__main__':
    main()