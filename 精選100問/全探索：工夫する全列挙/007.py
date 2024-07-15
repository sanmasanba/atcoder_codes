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
    N = int(input())
    Q = [tuple(map(int, input().split(' '))) for _ in range(N)]
    Q.sort()

    res = 0
    C = combinations(Q, 2)
    set_Q  =set(Q)
    # 2点間の距離を求める
    for p1, p2 in C:
        x1, y1 = p1
        x2, y2 = p2

        # 正方形の性質上、以下の計算式でp3、p4の位置が決まる
        p3 = x1 + y1-y2, y1 + x2-x1
        p4 = x2 + y1-y2, y2 + x2-x1

        # p3、p4が存在するなら正方形も存在する
        if p3 in set_Q and p4 in set_Q:
            res = max(res, (x2-x1)**2+(y2-y1)**2)
    print(res)

if __name__ == '__main__':
    main()