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
    Q = []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        Q.append([a, 0])
        Q.append([b, 1])
    # ソートする
    Q.sort()

    cnt = 0
    # t=時間, q=入退出
    for t, q in Q:
        # 入室
        if q == 0:
            # 人がいないならここから数え始める。
            if cnt == 0:
                print(t, end=(' '))
            cnt += 1                 
        # 退室
        else:
            cnt -= 1
            # 人がいないならここまでが一つの区間
            if cnt == 0:
                print(t)

if __name__ == '__main__':
    main()