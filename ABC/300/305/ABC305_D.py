#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
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
    cumsumA = [[0, 0]]
    # 累積和
    for i in range(1, N):
        tmp = cumsumA[-1]
        cumsumA.append([A[i], tmp[1] + (0 if i%2 else A[i]-A[i-1])])
    Q = int(input())
    res = []
    # シミュレーション
    for _ in range(Q):
        tmp = 0
        l, r = map(int, input().split(' '))
        # 全部寝ていた時間帯を求める
        l_pos, r_pos = bisect_left(A, l), bisect_left(A, r)
        tmp += cumsumA[r_pos-1][1] - cumsumA[l_pos][1]
        # 睡眠中に記録をつけ始めた時
        if not l_pos%2:
            tmp += A[l_pos] - l
        # 睡眠中に記録をやめた時
        if not r_pos%2:
            tmp += r - A[r_pos-1]
        res.append(tmp)
    for r in res:
        print(r)

if __name__ == '__main__':
    main()