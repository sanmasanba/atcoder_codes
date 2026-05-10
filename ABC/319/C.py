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
    C = []
    for _ in range(3):
        C += list(map(int, input().split(' ')))

    # 調べる列   
    check = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    # 0-9のパネルが何番目に開けられるか
    order = list(range(9))
    
    not_bad_cnt = 0
    cnt = 0
    # 全探索
    for per in permutations(order):
        cnt += 1
        flag = False
        # 判定
        for a, b, c in check:
            # aとbに同じ数字があって、最後にcが開けられたらアウト(同じ数字は3つは来ない)
            if C[a] == C[b] and per[a] < per[c] and per[b] < per[c]:
                flag = True
            # 他も一緒
            elif C[b] == C[c] and per[b] < per[a] and per[c] < per[a]:
                flag = True
            elif C[c] == C[a] and per[c] < per[b] and per[a] < per[b]:
                flag = True
        # うまくいったらカウント
        if not flag:
            not_bad_cnt += 1
    print(not_bad_cnt/cnt)

if __name__ == '__main__':
    main()