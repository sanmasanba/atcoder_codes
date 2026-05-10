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
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    # 各xの位置を保存する
    x_pos = {}
    for i, a in enumerate(A):
        if a not in x_pos:
            x_pos[a] = []
        x_pos[a].append(i)
    # クエリを処理する
    res = []
    for _ in range(Q):
        x, k = map(int, input().split(' '))
        # 要素に含まれないときと、k回もxが登場しないとき-1
        if x not in x_pos or len(x_pos[x]) < k:
            res.append(-1)
            continue
        else:
            res.append(x_pos[x][k-1]+1)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()