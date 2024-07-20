#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    P = [0] + [int(input()) for _ in range(N)]

    low = 0
    high = M
    combi = []
    # 2本投げたときのパターンを半分全列挙
    for i in P:
        for j in P:
            combi.append(i+j)
    # 二分探索用にソート
    combi.sort()

    # aを固定して、[0, M-a)の範囲で最大となるbを探索する
    res = 0
    for a in combi:
        b_pos = bisect_right(combi, M-a)
        if b_pos == 0:  continue
        res = max(res, a+combi[b_pos-1])
    print(res)

if __name__ == '__main__':
    main()