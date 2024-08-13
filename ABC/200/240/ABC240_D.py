#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    stack = [[0, 0]]
    balls = 0
    for a in A:
        # 一番上に積まれているボールが異なるとき、新しく積み上げて
        # ballの数をふやす
        if stack[-1][0] != a:
            stack.append([a, 1])
            balls += 1
        # 一番上に積まれているボールが同じとき、一番上を更新して
        # ballの数をふやす
        else:
            stack[-1][1] += 1
            balls += 1
        # 一番上のボールの数と数字が一致するとき、消して
        # ボールの数をその分減らす
        if stack[-1][0] == stack[-1][1]:
            stack.pop()
            balls -= a
        print(balls)

if __name__ == '__main__':
    main()