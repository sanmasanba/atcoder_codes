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
    A = list(map(int, input().split(' ')))

    # 要素の集合を取る
    A_set = sorted([x for x in set(A)])
    a_cnt = {}
    n = len(A_set)
    # 各要素より大きいものの数を記録
    cnt = 1
    for a in A_set:
        a_cnt[a] =  n-cnt
        cnt += 1

    # 出力
    res = [0 for _ in range(N)]
    for a in A:
        res[a_cnt[a]] += 1

    print(*res, sep='\n')

if __name__ == '__main__':
    main()